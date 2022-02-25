# conan-packages

First you need to create the packages and upload them to a conan remote that you control:

Run these commands:

```
conan create gcc_8.5.0_glibc_2.27_x86_64
conan upload gcc_8.5.0_glibc_2.27_x86_64 -r [my-remote]
conan create gcc_8.5.0_glibc_2.27_armhf
conan upload gcc_8.5.0_glibc_2.27_armhf -r [my-remote]
```