"""
Utilidades multiplataforma (macOS y Windows) para la resolución de rutas,
detección de OneDrive, creación de copias de seguridad y guardado dual del documento de tesis.
"""

import os
import platform
import shutil
import subprocess
from pathlib import Path
from typing import Optional

DOCUMENT_DEFAULT_NAME = "TESIS_FINAL_IS_V_2024_025_GOMEZ_PANTALEON.docx"
MARKDOWN_DEFAULT_NAME = "TESIS.md"

def get_platform_name() -> str:
    """Retorna el nombre del sistema operativo ('Darwin' = macOS, 'Windows' = Windows, 'Linux' = Linux)."""
    return platform.system()

def get_repo_root() -> Path:
    """Retorna la ruta absoluta de la raíz del repositorio local."""
    return Path(__file__).resolve().parent.parent

def get_workspace_path(filename: str = DOCUMENT_DEFAULT_NAME) -> Path:
    """Retorna la ruta absoluta del archivo dentro del espacio de trabajo del repositorio."""
    return get_repo_root() / filename

def find_onedrive_path(filename: str = DOCUMENT_DEFAULT_NAME) -> Optional[Path]:
    """
    Localiza de forma automática la ruta física del archivo en OneDrive
    tanto en macOS (Apple File Provider en CloudStorage) como en Windows (%OneDrive%).
    Retorna None si no se encuentra sincronizado en la máquina actual.
    """
    sys_name = get_platform_name()
    home = Path.home()

    if sys_name == "Darwin":  # macOS
        # Rutas estándar de Apple File Provider en macOS (Monterey, Ventura, Sonoma, Sequoia)
        candidates = [
            home / "Library/CloudStorage/OneDrive-Personal/Documentos" / filename,
            home / "Library/CloudStorage/OneDrive-Personal" / filename,
            home / "OneDrive/Documentos" / filename,
            home / "OneDrive" / filename,
        ]
        for cand in candidates:
            if cand.exists():
                return cand

        # Búsqueda dinámica en carpetas OneDrive dentro de CloudStorage
        cloud_storage = home / "Library/CloudStorage"
        if cloud_storage.exists():
            for entry in cloud_storage.glob("OneDrive*"):
                if entry.is_dir():
                    cand1 = entry / "Documentos" / filename
                    if cand1.exists():
                        return cand1
                    cand2 = entry / filename
                    if cand2.exists():
                        return cand2

    elif sys_name == "Windows":
        # Variables de entorno estándar de Windows
        env_vars = ["OneDriveConsumer", "OneDrive", "OneDriveCommercial", "USERPROFILE"]
        for var in env_vars:
            val = os.environ.get(var)
            if val:
                base = Path(val)
                candidates = [
                    base / "Documentos" / filename,
                    base / "Documents" / filename,
                    base / filename,
                    base / "OneDrive" / "Documentos" / filename,
                    base / "OneDrive" / filename,
                ]
                for cand in candidates:
                    if cand.exists():
                        return cand

        # Fallback a Registro de Windows para cuentas personales
        try:
            import winreg
            key_path = r"Software\Microsoft\OneDrive\Accounts\Personal"
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path) as key:
                user_folder, _ = winreg.QueryValueEx(key, "UserFolder")
                if user_folder:
                    cand1 = Path(user_folder) / "Documentos" / filename
                    if cand1.exists():
                        return cand1
                    cand2 = Path(user_folder) / filename
                    if cand2.exists():
                        return cand2
        except Exception:
            pass

    return None

def create_backup(source_path: Path) -> Path:
    """
    Crea una copia de seguridad inmediata con sufijo .backup.docx en el repositorio.
    """
    backup_path = get_workspace_path(f"{source_path.stem}.backup.docx")
    shutil.copy2(source_path, backup_path)
    print(f"[BACKUP] Copia de respaldo generada: {backup_path}")
    return backup_path

def dual_save(doc, filename: str = DOCUMENT_DEFAULT_NAME) -> tuple[Path, Optional[Path]]:
    """
    Guarda el objeto docx.Document de forma dual:
    1. En el repositorio local (workspace).
    2. En la ruta sincronizada de OneDrive (si está disponible en la máquina actual).
    """
    ws_path = get_workspace_path(filename)
    doc.save(str(ws_path))
    print(f"[DUAL-SAVE] Guardado en espacio de trabajo local: {ws_path}")

    od_path = find_onedrive_path(filename)
    if od_path:
        try:
            # En Windows o Mac, asegurar que el directorio padre exista
            od_path.parent.mkdir(parents=True, exist_ok=True)
            doc.save(str(od_path))
            print(f"[DUAL-SAVE] Guardado en OneDrive sincronizado: {od_path}")
        except (PermissionError, OSError) as e:
            print(f"[DUAL-SAVE] Aviso de permisos: No se pudo escribir en OneDrive ({e}). Requiere BypassSandbox o ejecución fuera del sandbox.")
    else:
        print(f"[DUAL-SAVE] Aviso: No se detectó ruta activa de OneDrive en {get_platform_name()}. Solo se guardó en local.")

    return ws_path, od_path

def evaluate_sync(file_path: Optional[Path]) -> None:
    """
    Evalúa el estado de sincronización con la nube según el sistema operativo.
    En macOS ejecuta fileproviderctl evaluate; en Windows inspecciona atributos.
    """
    if not file_path or not file_path.exists():
        print("[SYNC] Archivo no especificado o inexistente para evaluar.")
        return

    sys_name = get_platform_name()
    if sys_name == "Darwin":
        try:
            res = subprocess.run(
                ["fileproviderctl", "evaluate", str(file_path)],
                capture_output=True,
                text=True,
                timeout=10
            )
            if "isUploaded = 1" in res.stdout:
                print("[SYNC macOS] Sincronización verificada: el archivo está subido a la nube (isUploaded = 1).")
            elif "Syncing" in res.stdout or "isUploading = 1" in res.stdout:
                print("[SYNC macOS] El archivo se encuentra en proceso de subida (Syncing).")
            else:
                print(f"[SYNC macOS] fileproviderctl evaluado con código {res.returncode}.")
        except Exception as e:
            print(f"[SYNC macOS] No se pudo ejecutar fileproviderctl: {e}")
    elif sys_name == "Windows":
        # En Windows inspeccionar atributos o estado de Cloud Files
        try:
            import ctypes
            attrs = ctypes.windll.kernel32.GetFileAttributesW(str(file_path))
            # FILE_ATTRIBUTE_PINNED = 0x00080000; FILE_ATTRIBUTE_RECALL_ON_DATA_ACCESS = 0x00400000
            print(f"[SYNC Windows] Atributos NTFS del archivo en disco: {hex(attrs)}")
        except Exception as e:
            print(f"[SYNC Windows] Estado de archivo: presente en disco ({e})")
