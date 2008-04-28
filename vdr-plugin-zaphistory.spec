
%define plugin	zaphistory
%define name	vdr-plugin-%plugin
%define version	0.9.5
%define rel	8

Summary:	VDR plugin: History of the last zapped channels
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.unterbrecher.de/vdr/developer.php
Source:		http://www.unterbrecher.de/vdr/download/vdr-%plugin-%version.tar.bz2
Patch0:		zaphistory-0.9.5-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
