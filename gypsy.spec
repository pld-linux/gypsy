Summary:	Gypsy - a GPS multiplexing daemon
Name:		gypsy
Version:	0.7
Release:	1
Source0:	http://gypsy.freedesktop.org/gypsy-releases/%{name}-%{version}.tar.gz
# Source0-md5:	cde52c121693014efa75d9098fd7de22
Group:		Libraries
# See LICENSE file for details
License:	LGPLv2 and GPLv2
URL:		http://gypsy.freedesktop.org/
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk-doc
BuildRequires:	libxslt
BuildRequires:	pkgconfig
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gypsy is a GPS multiplexing daemon which allows multiple clients to
access GPS data from multiple GPS sources concurrently.

%package devel
Summary:	Development package for gypsy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel
Requires:	pkgconfig

%description devel
Header files for development with gypsy.

%package apidocs
Summary:	Documentation files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk-doc

%description apidocs
This package contains developer documentation for %{name}.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING.lib LICENSE
/etc/dbus-1/system.d/Gypsy.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.Gypsy.service
%{_libexecdir}/gypsy-daemon
%attr(755,root,root) %{_libdir}/libgypsy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgypsy.so.0

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/gypsy.pc
%{_includedir}/gypsy
%{_libdir}/libgypsy.so
%{_libdir}/libgypsy.la

%files apidocs
%defattr(644,root,root,755)
%doc %{_gtkdocdir}/gypsy
