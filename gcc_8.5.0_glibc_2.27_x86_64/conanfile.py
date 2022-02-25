from conan.tools.cmake import CMakeToolchain
from conans import ConanFile, tools
import os

class GccConan(ConanFile):
    name = "gcc_8.5.0_glibc_2.27_x86_64"
    version = "0.0.1"
    settings = "os", "arch"
    description = "<Description of LinaroGcc here>"
    url = "None"
    license = "None"
    author = "None"
    topics = None
    exports_sources = "x86_64-linux-gnu/*"

    def package(self):
        self.copy("*")

    def package_info(self):
        path = os.path.join(self.package_folder, "x86_64-linux-gnu")
        sysroot  = os.path.join(self.package_folder, "x86_64-linux-gnu/x86_64-linux-gnu/sysroot")

        self.user_info.PACKAGE_FOLDER = self.package_folder
        self.user_info.C_COMPILER = os.path.join(path, "bin/x86_64-linux-gnu-gcc")
        self.user_info.CXX_COMPILER = os.path.join(path, "bin/x86_64-linux-gnu-g++")
        self.user_info.SYSROOT = sysroot

        self.env_info.CC = os.path.join(path, "bin/x86_64-linux-gnu-gcc")
        self.env_info.CXX = os.path.join(path, "bin/x86_64-linux-gnu-g++")
        self.env_info.SYSROOT = sysroot
        self.env_info.CFLAGS   = "-fPIC            -O0 -ggdb -Wall"
        self.env_info.CXXFLAGS = "-fPIC -std=c++11 -O0 -ggdb -Wall"

        self.env_info.CONAN_CMAKE_SYSROOT = sysroot
        self.env_info.CONAN_CMAKE_FIND_ROOT_PATH = sysroot
        
        self.env_info.CONAN_CMAKE_FIND_ROOT_PATH_MODE_PROGRAM = "NEVER"
        self.env_info.CONAN_CMAKE_FIND_ROOT_PATH_MODE_LIBRARY = "ONLY"
        self.env_info.CONAN_CMAKE_FIND_ROOT_PATH_MODE_INCLUDE = "ONLY"
        self.env_info.CONAN_CMAKE_FIND_ROOT_PATH_MODE_PACKAGE = "ONLY"

