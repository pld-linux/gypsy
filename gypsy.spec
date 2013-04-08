# TODO:
# - --with-user= (not root!) - is nobody OK, or some more specific user required?
Summary:	Gypsy - a GPS multiplexing daemon
Summary(pl.UTF-8):	Gypsy - demon przełączający dostęp do GPS
Name:		gypsy
Version:	0.9
Release:	1
License:	LGPL v2+ (library), GPL v2+ (daemon)
Group:		Daemons
Source0:	http://gypsy.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	e2d186df9c2cc3b70a027043e22acf1a
Patch0:		%{name}-link.patch
Patch1:		gypsy-0.8-unusedvar.patch
Patch2:		%{name}-glib.patch
URL:		http://gypsy.freedesktop.org/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	bluez-libs-devel
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	gtk-doc >= 1.6
BuildRequires:	libtool
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gypsy is a GPS multiplexing daemon which allows multiple clients to
access GPS data from multiple GPS sources concurrently.

%description -l pl.UTF-8
Gypsy to demon multipleksujący GPS, pozwalający wielu klientom na
naprzemienny dostęp do danych GPS z wielu źródeł.

%package libs
Summary:	Gypsy library
Summary(pl.UTF-8):	Biblioteka gypsy
Group:		Libraries
Conflicts:	gypsy < 0.8

%description libs
Gypsy GPS multiplexing library.

%description libs -l pl.UTF-8
Biblioteka gypsy multipleksująca dostęp do usługi GPS.

%package devel
Summary:	Development package for gypsy
Summary(pl.UTF-8):	Pakiet programistyczny gypsy
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.60

%description devel
Header files for development with gypsy.

%description devel -l pl.UTF-8
Pliki nagłówkowe do programowania z użyciem gypsy

%package static
Summary:	Static gypsy library
Summary(pl.UTF-8):	Statyczna biblioteka gypsy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gypsy library.

%description static -l pl.UTF-8
Statyczna biblioteka gypsy.

%package apidocs
Summary:	Gypsy API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gypsy
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
This package contains developer documentation for gypsy.

%description apidocs -l pl.UTF-8
Dokumentacja programisty do gypsy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/gypsy-daemon
/etc/dbus-1/system.d/Gypsy.conf
/etc/gypsy.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.Gypsy.service

%files libs
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS TODO
%attr(755,root,root) %{_libdir}/libgypsy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgypsy.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgypsy.so
%{_libdir}/libgypsy.la
%{_includedir}/gypsy
%{_pkgconfigdir}/gypsy.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgypsy.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gypsy
