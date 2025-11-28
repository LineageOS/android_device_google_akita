#
# SPDX-FileCopyrightText: 2021 The Android Open-Source Project
# SPDX-License-Identifier: Apache-2.0
#

$(call inherit-product, device/google/zuma/aosp_common.mk)
$(call inherit-product, device/google/akita/device-akita.mk)

PRODUCT_NAME := aosp_akita
PRODUCT_DEVICE := akita
PRODUCT_MODEL := AOSP on akita
PRODUCT_BRAND := Android
PRODUCT_MANUFACTURER := Google
