Name:           ros-indigo-nao-vision
Version:        0.1.5
Release:        0%{?dist}
Summary:        ROS nao_vision package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/nao_vision
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-nao-interaction-msgs
Requires:       ros-indigo-roslaunch
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
BuildRequires:  ros-indigo-catkin

%description
Package for the Nao robot, providing access to NAOqi vision proxies

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Dec 14 2014 Manos Tsardoulias <etsardou@gmail.com> - 0.1.5-0
- Autogenerated by Bloom

* Thu Nov 13 2014 Manos Tsardoulias <etsardou@gmail.com> - 0.1.4-0
- Autogenerated by Bloom

* Mon Sep 08 2014 Manos Tsardoulias <etsardou@gmail.com> - 0.1.3-0
- Autogenerated by Bloom

* Sun Sep 07 2014 Manos Tsardoulias <etsardou@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

* Sun Sep 07 2014 Manos Tsardoulias <etsardou@gmail.com> - 0.1.2-0
- Autogenerated by Bloom

