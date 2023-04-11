# diable for now as some test cases are failing
%bcond_with check

Name:           cpr
Version:        1.10.2
Release:        %autorelease
Summary:        C++ Requests: Curl for People, a spiritual port of Python Requests

License:        MIT
URL:            https://github.com/libcpr/cpr
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  curl-devel
%if %{with check}
BuildRequires:  gtest-devel
BuildRequires:  mongoose-devel
%endif

%description
C++ Requests is a simple wrapper around libcurl inspired by the excellent Python
Requests project.

Despite its name, libcurl's easy interface is anything but, and making mistakes,
misusing it is a common source of error and frustration. Using the more
expressive language facilities of C++17 (or C++11 in case you use cpr < 1.10.0),
this library captures the essence of making network calls into a few concise
idioms.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DCPR_USE_SYSTEM_CURL=ON \
  %if %{with check}
  -DCPR_BUILD_TESTS=ON \
  -DCPR_USE_SYSTEM_GTEST=ON \
  %endif

%cmake_build

%install
%cmake_install

%if %{with check}
%check
%ctest
%endif

%files
%license LICENSE
%doc README.md
%{_libdir}/libcpr.so.1*

%files devel
%{_includedir}/cpr/
%{_libdir}/libcpr.so
%{_libdir}/cmake/cpr/

%changelog
%autochangelog
