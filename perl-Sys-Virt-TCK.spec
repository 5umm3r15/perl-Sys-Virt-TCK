# Automatically generated by perl-Sys-Virt-TCK.spec.PL

%define appname Sys-Virt-TCK

Summary: Sys::Virt::TCK - libvirt Technology Compatibility Kit
Name: perl-%{appname}
Version: 1.0.0
Release: 1
License: GPLv2
Source: http://libvirt.org/sources/tck/%{appname}-v%{version}.tar.gz
Url: http://libvirt.org/
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires: libvirt >= 4.4.0
%if 0%{?fedora} || 0%{?rhel} > 7
BuildRequires: perl-interpreter
BuildRequires: perl-generators
%endif
BuildRequires: perl(accessors)
BuildRequires: perl(App::Prove)
BuildRequires: perl(Config::Record)
BuildRequires: perl(Cwd)
BuildRequires: perl(File::Spec::Functions)
BuildRequires: perl(File::Copy)
BuildRequires: perl(File::Path)
BuildRequires: perl(File::Slurp)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(IO::String)
BuildRequires: perl(IO::Uncompress::Gunzip)
BuildRequires: perl(IO::Uncompress::Bunzip2)
BuildRequires: perl(Module::Build)
BuildRequires: perl(TAP::Formatter::HTML)
BuildRequires: perl(TAP::Formatter::JUnit)
BuildRequires: perl(TAP::Harness)
BuildRequires: perl(TAP::Harness::Archive)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::More)
BuildRequires: perl(Sub::Uplevel)
BuildRequires: perl(Sys::Virt) >= 0.2.1
BuildRequires: perl(XML::Twig)
BuildRequires: perl(XML::Writer)
BuildRequires: perl(XML::XPath)
BuildRequires: perl(Test::Pod)
BuildRequires: perl(Test::Pod::Coverage)
# RPM autoprovides misses these 3
Requires: perl(Test::Exception)
Requires: perl(TAP::Formatter::HTML)
Requires: perl(TAP::Formatter::JUnit)
Requires: perl(TAP::Harness::Archive)
Requires: perl(Net::OpenSSH)
Requires: perl(IO::Pty)
Requires: libguestfs-tools
Requires: /usr/bin/mkisofs
# Want to force this minimal version, so don't rely on RPM autoprov
Requires: perl(Sys::Virt) >= 0.2.1
BuildArchitectures: noarch

%description
Sys::Virt::TCK provides an integration test suite for validating
correct operation of libvirt drivers with underlying virtualization
technology.

%prep
%setup -q -n %{appname}-v%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0 \
  --install_path conf=%{_sysconfdir}/libvirt-tck \
  --install_path pkgdata=%{_datadir}/libvirt-tck/tests

find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%__install -m 0755 -d $RPM_BUILD_ROOT%{_localstatedir}/cache/libvirt-tck

%files
%defattr(-,root,root)
%license LICENSE
%doc README Changes
%dir %{_sysconfdir}/libvirt-tck
%config(noreplace) %{_sysconfdir}/libvirt-tck/default.cfg
%{_bindir}/libvirt-tck
%dir %{_datadir}/libvirt-tck
%{_datadir}/libvirt-tck/*
%{_mandir}/man1/*
%{perl_vendorlib}/Sys/Virt/TCK.pm
%{perl_vendorlib}/Sys/Virt/TCK/
%dir %{_localstatedir}/cache/libvirt-tck

%changelog
* Mon Jun 11 2018 Daniel P. Berrangé <berrange@redhat.com> - 1.0.0-1
- Update to 1.0.0 release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.0-24
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.1.0-22
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
