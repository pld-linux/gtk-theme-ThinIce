Summary:	Flat theme without distracting stuff
Summary(pl):	P³aski temat bez zbêdnych drobiazgów
Name:		gtk-theme-ThinIce
Version:	1.0.4
Release:	1
License:	GPL
Group:		Themes/Gtk
Source0:	ThinIce-1.2.x.tar.gz
URL:		http://gtk.classic.themes.org/php/download.phtml?object=gtk.theme.934184517&rev=1.2.x
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

%description
Flat theme without distracting stuff.

%description -l pl
P³aski temat bez zbêdnych drobiazgów.

%prep
%setup  -q -n gtk-thinice-theme-%{version}

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk/themes/engines/*.so
%{_datadir}/themes/ThinIce
