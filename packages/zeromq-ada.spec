%define debug_package %{nil}

Name:       zeromq-ada
Version:    4.1.5
Release:    1.git%{?dist}
Summary:    Ada binding for zeromq
License:    GPLv2+
URL:        http://zeromq.org
## Source from github. for get source use 
## https://github.com/reznikmm/zeromq-Ada/archive/4.1.5-20200330.tar.gz
Source0:    zeromq-ada.tar.gz
## Use shared libs instead static
#Patch0:     {name}-libdir.patch
## Use directories.gpr
#Patch1:     {name}-fedora.patch
BuildRequires: fedora-gnat-project-common >= 2 zeromq-devel >= 2.1
BuildRequires: chrpath gcc-gnat gprbuild
Requires:    zeromq >= 2.1
# gcc-gnat only available on these:
ExclusiveArch: %{GPRbuild_arches}

%description
Ada bindings for zeromq

%package devel
Summary:        Devel package for Ada binding for zeromq
License:        GPLv2+
Requires:       fedora-gnat-project-common  >= 2
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zeromq-devel >= 2.1

%description devel
%{summary}
%prep
%setup -q -n zeromq-Ada
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
touch Makefile.config
cp -v libsodium.gpr.in libsodium.gpr
cp -v libzmq.gpr.in libzmq.gpr
patch Makefile packages/%{name}-libdir.patch
patch zmq.gpr.inst packages/%{name}-fedora.patch

%build
make %{?_smp_mflags}  GNATFLAGS="%{GNAT_optflags}"  GNATMAKE="gprbuild -p -R %{GNAT_optflags}" PREFIX=/usr
## for tests aunit needed


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} LIBDIR=%{_libdir} ADA_PROJECT_DIR=%{_GNAT_project_dir}  GNATFLAGS="%{GNAT_optflags}" PREFIX=/usr
rm -f %{buildroot}/%{_libdir}/zmq/static/libzmqAda.a
rm -rf %{buildroot}/%{_libdir}/zmq/static
chrpath --delete %{buildroot}%{_libdir}/zmq/relocatable/libzmqAda.so.%{version}

%ldconfig_scriptlets

%files
%doc README.md COPYING
%dir %{_libdir}/zmq
%dir %{_libdir}/zmq/relocatable
%{_libdir}/zmq/relocatable/libzmqAda.so.%{version}
%{_libdir}/libzmqAda.so.*


%files devel
%{_libdir}/zmq/relocatable/libzmqAda.so
%{_libdir}/libzmqAda.so
%dir %{_includedir}/zmq/
%{_includedir}/zmq/*.adb
%{_includedir}/zmq/*.ads
%{_GNAT_project_dir}/zmq.gpr
%{_libdir}/zmq/relocatable/*.ali
%{_datadir}/zmq/*

%changelog
* Wed Jun 17 2020 Max Reznik <reznikmm@gmail.com> - 4.1.5-1.git
- Update to 4.1.5

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-30.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-29.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-28.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-27.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Pavel Zhukov <landgraf@fedoraproject.org - 2.1.0-26.24032011git
- rebuilt with new gnat
- Use gprbuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-23.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-22.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 2.1.0-21.24032011git
- Rebuilt for libgnat soname bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-20.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 23 2015 Thomas Spura <tomspur@fedoraproject.org> - 2.1.0-19.24032011git
- rebuilt for new zeromq 4.1.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-18.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 26 2015 Kalev Lember <kalevlember@gmail.com> - 2.1.0-17.24032011git
- Rebuilt for new libgnat

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-16.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-15.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0-14.24032011git
- Use GNAT_arches rather than an explicit list

* Sun Apr 20 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-13.24032011git
- Rebuild with new GCC 

* Sun Mar 02 2014 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-12.24032011git
- Fix library finalization. https://github.com/persan/zeromq-Ada/issues/10

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-11.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jan 25 2013 Kevin Fenzi <kevin@scrye.com> 2.1.0-10.24032011git
- Rebuild for new libgnat
- Add buildrequires on gcc-gnat. It's no longer pulled in by fedora-gnat-project-common

* Sun Sep 23 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-9.24032011git
- Fix gpr path

* Sun Sep 23 2012 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-8.24032011git
- Fix libraries symlinks
- Add usrmove patch

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-7.24032011git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 05 2011 Dan Horák <dan[at]danny.cz> - 2.1.0-6.24032011git
- updated the supported arch list

* Fri Apr 29 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-4.24032011git
- Create shared libraries path
- Fix license tag
- Fix spec errors

* Thu Mar 24 2011 Pavel Zhukov <landgraf@fedoraproject.org> - 2.1.0-1.24032011git
- update to new commit

* Wed Feb 2 2011 Pavel Zhukov <pavel@zhukoff.net> - 2.0.10-02022011git
- Initial package
