from conan import ConanFile
from conans import tools
import os
from conan.tools.cmake import CMakeToolchain

class GccConan(ConanFile):
    name = "gcc_8.5.0_glibc_2.27_armhf"
    version = "0.0.1"
    settings = "os", "arch"
    description = "<Description of LinaroGcc here>"
    url = "None"
    license = "None"
    author = "None"
    topics = None
    exports_sources = "arm-linux-gnueabihf/*"

    def package(self):
        self.copy("*")

    def package_info(self):
        path = os.path.join(self.package_folder, "arm-linux-gnueabihf")
        sysroot  = os.path.join(self.package_folder, "arm-linux-gnueabihf/arm-linux-gnueabihf/sysroot")

        self.user_info.PACKAGE_FOLDER = self.package_folder
        self.user_info.C_COMPILER = os.path.join(path, "bin/arm-linux-gnueabihf-gcc")
        self.user_info.CXX_COMPILER = os.path.join(path, "bin/arm-linux-gnueabihf-g++")
        self.user_info.SYSROOT = sysroot
        
        self.env_info.CC = os.path.join(path, "bin/arm-linux-gnueabihf-gcc")
        self.env_info.CXX = os.path.join(path, "bin/arm-linux-gnueabihf-g++")
        self.env_info.SYSROOT = sysroot
        self.env_info.CFLAGS   = "-fPIC            -mfloat-abi=hard -O0 -ggdb -Wall -Wno-psabi"
        self.env_info.CXXFLAGS = "-fPIC -std=c++11 -mfloat-abi=hard -O0 -ggdb -Wall -Wno-psabi"

        self.env_info.CONAN_CMAKE_SYSROOT = sysroot
        self.env_info.CONAN_CMAKE_FIND_ROOT_PATH = sysroot

        self.env_info.CONAN_CMAKE_FIND_ROOT_PATH_MODE_PROGRAM = "NEVER"
        self.env_info.CONAN_CMAKE_FIND_ROOT_PATH_MODE_LIBRARY = "ONLY"
        self.env_info.CONAN_CMAKE_FIND_ROOT_PATH_MODE_INCLUDE = "ONLY"
        self.env_info.CONAN_CMAKE_FIND_ROOT_PATH_MODE_PACKAGE = "ONLY"

