%bcond_without qt6

Name:           nodeeditor
Version:        3.0.10
Release:        %autorelease
Summary:        Qt Node Editor. Dataflow programming framework
License:        BSD-Protection
URL:            https://github.com/paceholder/nodeeditor
Source:         %{url}/archive/%{version}/folly-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
%if %{with qt6}
# find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Core Widgets Gui OpenGL)
BuildRequires:	cmake(Qt6Core)  
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6OpenGL)
%else
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5OpenGL)
%endif

# for testing
%if %{?fedora} <= 38
BuildRequires:  catch-devel
%else
BuildRequires:  catch2-devel
%endif

%description
QtNodes is conceived as a general-purpose Qt-based library aimed at developing 
Node Editors for various applications. The library could be used for simple 
graph visualization and editing or extended further for using the Dataflow 
paradigm .

%prep
%autosetup

%build
%cmake \
  -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md


%changelog
%autochangelog
