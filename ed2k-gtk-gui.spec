#
# Conditional build:
# _without_core - use it if you will have own edonkey2000 core
#
Summary:	eDonkey2000 P2P Network Client
Summary(pl):	Klient sieci eDonkey2000
Name:		ed2k-gtk-gui
Version:	0.5.0
Release:	4
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/%{name}/%{name}_%{version}.tar.gz
# Source0-md5:	c71d47f9d591624d468758dde2463e46
URL:		http://ed2k-gtk-gui.sourceforge.net/
BuildRequires:	gnet-devel < 1.2.0
BuildRequires:	gtk+-devel
BuildRequires:	libxml2-devel
BuildRequires:	zlib-devel
%{!?_without_core:Requires: eDonkey-core}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_docdir		/usr/X11R6/share

%description
GTK+ GUI for eDonkey2000 or overnet core client.

%description -l pl
Nak³adka na rdzeñ klienta sieci eDonkey2000 lub sieci overnet.

%prep
%setup -q -n ed2k-gtk-gui_%{version}

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f ed2k_gui/docs/en/Makefile*

%find_lang ed2k_gui

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo""
echo "Please type edonkey-conf, when you'll be logged as user"
echo "It will prepare your donkey to use with ed2k :)"
echo ""
echo "You may also type overnet-conf, it will prepare overnet-core"
echo "to use with ed2k, more info at http://www.overnet.com/"
echo ""

%files -f ed2k_gui.lang
%defattr(644,root,root,755)
%doc README ChangeLog BUGS AUTHORS ed2k_gui/docs/en/
%attr(755,root,root) %{_bindir}/*
%{_datadir}/ed2k_gui
