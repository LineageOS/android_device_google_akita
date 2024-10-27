#!/usr/bin/env -S PYTHONPATH=../../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.file import File, FileArgs, FileList
from extract_utils.fixups_blob import (
    BlobFixupCtx,
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixup_remove,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

from extract_utils.extract import extract_fns_user_type
from extract_utils.extract_pixel import (
    copy_pixel_firmware,
    extract_pixel_factory_image,
    extract_pixel_firmware,
    pixel_factory_image_regex,
    pixel_firmware_regex,
)

namespace_imports = [
    'device/google/akita',
    'hardware/google/av',
    'hardware/google/gchips',
    'hardware/google/graphics/common',
    'hardware/google/interfaces',
    'hardware/google/pixel',
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}-{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'com.google.edgetpu_app_service-V4-ndk',
        'com.google.edgetpu_vendor_service-V2-ndk',
    ): lib_fixup_vendor_suffix,
    (
        'libacryl',
        'libexynosv4l2',
    ): lib_fixup_remove,
}


def blob_fixup_test_flag(
    ctx: BlobFixupCtx,
    file: File,
    file_path: str,
    *args,
    **kargs,
):
    with open(file_path, 'rb+') as f:
        f.seek(1337)
        f.write(b'\x01')


blob_fixups: blob_fixups_user_type = {
    'vendor/etc/init/init.modem_logging_control.rc': blob_fixup()
        .regex_replace(' && property:ro.debuggable=0', ''),
    'product/etc/felica/common.cfg': blob_fixup()
        .patch_file('osaifu-keitai.patch'),
}  # fmt: skip

extract_fns: extract_fns_user_type = {
    pixel_factory_image_regex: extract_pixel_factory_image,
    pixel_firmware_regex: [
        copy_pixel_firmware,
        extract_pixel_firmware,
    ],
}

module = ExtractUtilsModule(
    'akita',
    'google',
    device_rel_path='device/google/akita/akita',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_generated_carriersettings=True,
    add_firmware_proprietary_file=True,
    add_factory_proprietary_file=True,
    extract_fns=extract_fns,
    check_elf=True,
)


def fix_vendor_file_list(file_list: FileList):
    disable_checkelf_file_paths = [
        'vendor/lib64/libExynosC2H263Dec.so',
        'vendor/lib64/libExynosC2H263Enc.so',
        'vendor/lib64/libExynosC2H264Dec.so',
        'vendor/lib64/libExynosC2H264Enc.so',
        'vendor/lib64/libExynosC2HevcDec.so',
        'vendor/lib64/libExynosC2HevcEnc.so',
        'vendor/lib64/libExynosC2Mpeg4Dec.so',
        'vendor/lib64/libExynosC2Mpeg4Enc.so',
        'vendor/lib64/libExynosC2Vp8Dec.so',
        'vendor/lib64/libExynosC2Vp8Enc.so',
        'vendor/lib64/libExynosC2Vp9Dec.so',
        'vendor/lib64/libExynosC2Vp9Enc.so',
    ]

    for file_path in disable_checkelf_file_paths:
        file_list.get_file(file_path).set_arg(FileArgs.DISABLE_CHECKELF, True)

    module_suffix_file_paths = [
        'vendor/lib64/com.google.edgetpu_app_service-V4-ndk.so',
        'vendor/lib64/com.google.edgetpu_vendor_service-V2-ndk.so',
    ]

    for file_path in module_suffix_file_paths:
        file_list.get_file(file_path).set_arg(FileArgs.MODULE_SUFFIX, '-vendor')


module.add_generated_proprietary_file(
    'proprietary-files-vendor.txt',
    partition='vendor',
    skip_file_list_name='skip-files-vendor.txt',
    fix_file_list=fix_vendor_file_list,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
