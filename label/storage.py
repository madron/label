import os
import flet as ft
from platform import platform as get_platform
from pathlib import Path, PurePath, PurePosixPath, PureWindowsPath
from label.constants import APP_NAME


def get_default_storage_path(platform=None) -> PurePath:
    platform = platform or get_platform()
    if platform == 'ios':
        raise NotImplementedError()
    elif platform == 'android':
        raise NotImplementedError()
    elif platform == 'win':
        base_path = PureWindowsPath(os.environ['APPDATA'])
    elif platform == 'macosx':
        base_path = PurePosixPath('~', 'Library', 'Application Support')
    else:
        base_path = PurePosixPath(os.environ.get('XDG_CONFIG_HOME', '~/.local/share'))
    return base_path / APP_NAME


def get_storage_path(page: ft.Page) -> PurePath:
    if page.client_storage.contains_key('label_storage_path'):
        path = Path(page.client_storage.get('label_storage_path'))
    else:
        path = Path(get_default_storage_path())
        page.client_storage.set('label_storage_path', str(path))
    path = path.expanduser()
    if not path.exists():
        path.mkdir(parents=True)
    return path
