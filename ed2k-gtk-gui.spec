#
# conditional build:
#
# _without_core - use it if you will have own edonkey2000 core
#
%define		ed2k_rel	1
Summary:	eDonkey2000 P2P Network Client
Summary(pl):	Klient sieci eDonkey2000
Name:		ed2k-gtk-gui
Version:	0.4.0
Release:	2
License:	GPL
Group:		Applications/Communications
Source0:	http://download.sourceforge.net/%{name}/%{name}_%{version}-%{ed2k_rel}.tar.gz
URL:		http://ed2k-gtk-gui.sourceforge.net/
BuildRequires:	gtk+-devel
BuildRequires:	libxml2-devel
BuildRequires:	zlib-devel
BuildRequires:	gnet-devel
%{!?_without_core:Requires: edonkey2k-core}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define		_docdir		/usr/X11R6/share

%description
eDonkey2000 P2P Network Client.

%description -l pl
Klient sieci eDonkey2000.

%prep
%setup -q -n ed2k_gui-%{version}

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm -f ed2k_gui/docs/en/Makefile*
%find_lang ed2k_gui

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo""
echo "Please type edonkey-conf, when you'll be logged as user"
echo "It will prepare your donkey to use with ed2k :)"
echo ""

%files -f ed2k_gui.lang
%defattr(644,root,root,755)
%doc README ChangeLog BUGS AUTHORS ed2k_gui/docs/en/
%attr(755,root,root) %{_bindir}/*
%{_datadir}/ed2k_gui/*
