#
# Conditional build:
# _without_core - use it if you will have own edonkey2000 core
#
Summary:	eDonkey2000 P2P Network Client
Summary(pl):	Klient sieci eDonkey2000
Name:		ed2k-gtk-gui
Version:	0.6.1
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	4e4644a77d97e88a9e474efef52fbd8b
URL:		http://ed2k-gtk-gui.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnet-devel >= 2.0.0
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	zlib-devel
%{!?_without_core:Requires: eDonkey-core}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GTK+ GUI for eDonkey2000 or overnet core client.

%description -l pl
Nak³adka na rdzeñ klienta sieci eDonkey2000 lub sieci Overnet.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f docs/{de,en,es}/Makefile*

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
%doc README ChangeLog TODO AUTHORS docs/en
%lang(de) %doc docs/de
%lang(es) %doc docs/es
%{_mandir}/man1/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/ed2k_gui
%{_desktopdir}/*
