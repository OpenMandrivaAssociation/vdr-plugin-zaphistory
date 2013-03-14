
%define plugin	zaphistory
%define name	vdr-plugin-%plugin
%define version	0.9.5
%define rel	11

Summary:	VDR plugin: History of the last zapped channels
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.unterbrecher.de/vdr/developer.php
Source:		http://www.unterbrecher.de/vdr/download/vdr-%plugin-%version.tar.bz2
Patch0:		zaphistory-0.9.5-i18n-1.6.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Originally the plugins provided a history of the latest viewed
channels. Since version 0.0.3 statistics (zaps and watchtime) are
collected for each channel. History can be sorted by latest viewed,
zap count and watch time. The idea is a self-learning favourites
list. The history provides a channel name + EPG view and a channel
name + statistics view. Statistics and history entries can be
deleted or reseted from the menu.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY


%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.9.5-10mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.9.5-9mdv2009.1
+ Revision: 359389
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.9.5-8mdv2009.0
+ Revision: 198002
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.9.5-7mdv2009.0
+ Revision: 197747
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.9.5-6mdv2008.1
+ Revision: 145270
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.9.5-5mdv2008.1
+ Revision: 103254
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.9.5-4mdv2008.0
+ Revision: 50066
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.9.5-3mdv2008.0
+ Revision: 42149
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.9.5-2mdv2008.0
+ Revision: 22730
- rebuild for new vdr

* Sat Apr 21 2007 Anssi Hannula <anssi@mandriva.org> 0.9.5-1mdv2008.0
+ Revision: 16458
- initial Mandriva release
- Created package structure for vdr-plugin-zaphistory.

