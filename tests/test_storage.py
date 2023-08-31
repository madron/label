import os
from pathlib import PurePosixPath, PureWindowsPath
from unittest import mock, TestCase
from label.storage import get_default_storage_path


class GetDefaultStoragePathTest(TestCase):
    def test_android(self):
        with self.assertRaises(NotImplementedError):
            get_default_storage_path(platform='android')

    def test_ios(self):
        with self.assertRaises(NotImplementedError):
            get_default_storage_path(platform='ios')

    @mock.patch.dict(os.environ, dict(APPDATA='C:\\Users\\bob\\AppData\\Roaming'))
    def test_win(self):
        path = get_default_storage_path(platform='win')
        self.assertEqual(path, PureWindowsPath('C:\\Users\\bob\\AppData\\Roaming\\label'))

    def test_macosx(self):
        path = get_default_storage_path(platform='macosx')
        self.assertEqual(path, PurePosixPath('~/Library/Application Support/label'))

    def test_unix(self):
        path = get_default_storage_path(platform='unix')
        self.assertEqual(path, PurePosixPath('~/.local/share/label'))

    @mock.patch.dict(os.environ, dict(XDG_CONFIG_HOME='~/Documents'))
    def test_unix_xdg(self):
        path = get_default_storage_path(platform='unix')
        self.assertEqual(path, PurePosixPath('~/Documents/label'))
