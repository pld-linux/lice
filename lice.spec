Summary:	Very functional script for EPIC
Summary(pl):	Bardzo funkcjonalny skrypt do EPIC
Name:		lice
Version:	4.2.0
Release:	4	
License:	GPL
Group:		Applications/Communications
Source0:	%{name}420.tar.gz
Source1:	%{name}420-polish-help.tar.gz
Patch0:		%{name}-global.patch
Patch1:		%{name}-windows-numbers.patch
Patch2:		%{name}-screencrash.patch
Patch3:		%{name}-newepic-themefix.patch
URL:		http://lice.codehack.com/
Requires:	epic4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LiCe is a script designed for the ircII and EPIC irc clients; it
radically improves the usability of these clients, providing features
and enhancements that pioneered the way for a whole crowd of
imitators. Though there is now much diversity, thousands of LiCe users
still declare it the best script ever.

%description -l pl
LiCe jest skryptem przeznaczonym do pracy z klientem irca EPIC. Jest
to bardzo funkcjonalny i popularny skrypt, oferuj±cy wiele przydatnych
cech i w³a¶ciwo¶ci.

%prep
%setup -q -a 0 -n .irc
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/epic/{userhelp,script/{lice,pics,themes}}

install *.reasons lice.* $RPM_BUILD_ROOT%{_datadir}/epic/script/
install lice/* $RPM_BUILD_ROOT%{_datadir}/epic/script/lice/
install pics/* $RPM_BUILD_ROOT%{_datadir}/epic/script/pics/
install themes/* $RPM_BUILD_ROOT%{_datadir}/epic/script/themes/
install userhelp/* $RPM_BUILD_ROOT%{_datadir}/epic/userhelp/

install -d polish-help doc/polish-help
mv -f help doc
mv -f doc/help/*.gz doc

tar xzf %{SOURCE1} -C polish-help
mv -f polish-help/.irc/* doc/polish-help
ln -sf %{_datadir}/doc/%{name}-%{version}/help $RPM_BUILD_ROOT%{_datadir}/epic/script/help

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*
%{_datadir}/epic/script/lice.*
%{_datadir}/epic/script/*.reasons
%{_datadir}/epic/script/help
%{_datadir}/epic/script/lice
%{_datadir}/epic/script/pics
%{_datadir}/epic/script/themes
%{_datadir}/epic/userhelp
