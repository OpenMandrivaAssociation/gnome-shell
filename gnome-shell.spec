# To make GNOME Shell extensions load, we need to get rid of DT_RUNPATH on /usr/bin/gnome-shell
# (see glibc bug #13945, GNOME bug #670477, Mageia bug #4523)
%define _disable_ld_enable_new_dtags 1

Summary:	Next generation GNOME desktop shell
Name:		gnome-shell
Version:	3.7.2
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
Url:		http://live.gnome.org/GnomeShell
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-shell/3.7/%{name}-%{version}.tar.xz
Patch1:		gnome-shell-3.6.2-new-favorites.patch

BuildRequires: intltool >= 0.40
BuildRequires: rootcerts, gtk-doc
BuildRequires: polkit-1-devel
BuildRequires: pkgconfig(clutter-1.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(folks)
BuildRequires: pkgconfig(gcr-3)
BuildRequires: pkgconfig(gjs-1.0) >= 1.34
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(gnome-bluetooth-1.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libedataserverui-3.0)
BuildRequires: pkgconfig(libgnome-menu-3.0) >= 3.6.0
BuildRequires: pkgconfig(libmutter) >= %{version}
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnm-util)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(telepathy-glib)
BuildRequires: pkgconfig(telepathy-logger-0.2)
BuildRequires: xsltproc
BuildConflicts: libevolution-data-server2-devel

Requires: at-spi2-atk
Requires: gjs
Requires: glxinfo
Requires: gnome-session
Requires: gtk+3.0
Requires: json-glib
Requires: librsvg
Requires: mutter

# md until js & python typelib autoreqs works
Requires: typelib(AccountsService)
Requires: typelib(Caribou)
Requires: typelib(ClutterX11) 
Requires: typelib(DBusGLib)
Requires: typelib(Folks)
Requires: typelib(Gcr)
Requires: typelib(Gkbd)
Requires: typelib(GDesktopEnums)
Requires: typelib(Gee)
Requires: typelib(GMenu)
Requires: typelib(GnomeBluetoothApplet)
Requires: typelib(Meta)
Requires: typelib(NMClient)
Requires: typelib(NetworkManager)
Requires: typelib(Polkit)
Requires: typelib(Soup)
Requires: typelib(TelepathyGLib)
Requires: typelib(TelepathyLogger)
Requires: typelib(UPowerGlib)

%description
The GNOME Shell redefines user interactions with the GNOME desktop. In
particular, it offers new paradigms for launching applications,
accessing documents, and organizing open windows in GNOME. Later, it
will introduce a new applets eco-system and offer new solutions for
other desktop features, such as notifications and contacts
management. The GNOME Shell is intended to replace functions handled
by the GNOME Panel and by the window manager in previous versions of
GNOME. The GNOME Shell has rich visual effects enabled by new
graphical technologies.

%package docs
Summary:        Documentation for %{name}
Group:          Books/Computer books
BuildArch:      noarch

%description docs
This package contains the documentation for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-compile-warnings=no

%make LIBS='-lgmodule-2.0'

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name}

%files -f %{name}.lang
%doc README 
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/mozilla/plugins/*.so
%{_libexecdir}/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell-hotplug-sniffer
%{_libexecdir}/gnome-shell-perf-helper
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/gnome-shell-extension-prefs.desktop
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/GConf/gsettings/gnome-shell-overrides.convert
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/%{name}
%{_datadir}/applications/evolution-calendar.desktop
%{_mandir}/man1/%{name}.1*

%files docs
%{_datadir}/gtk-doc/html/shell
%{_datadir}/gtk-doc/html/st



%changelog
* Sun Nov 25 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.2-2
- also add rpmdrake to favorite panel

* Tue Nov 13 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.2-1
- update to 3.6.2

* Mon Oct 15 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-3
- chromium by default

* Fri Oct 12 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-2
- fix typo in function name, caught on auth error (bgo#685434)

* Tue Oct  2 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Fri Jul 20 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.2-1
+ Revision: 810475
- update to new version 3.4.2

* Mon May 07 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.1-2
+ Revision: 797302
- rebuild added missing typelib reqs

* Wed May 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.1-1
+ Revision: 794895
- remove old schemas
- new version 3.4.1

* Tue Apr 03 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.2.1-3
+ Revision: 788916
- rebuild
- added deps for gir pkgs

* Sun Mar 18 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.2.1-2
+ Revision: 785463
- rebuild
- added requires to make sure proper apps get installed
- remove old preview session
- cleaned up spec

* Mon Mar 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.2.1-1
+ Revision: 782135
- gnome-bluetooth support disabled for now
- unable to build
- added patch for gnome-bluetooth-applet
- new version 3.2.2.1
- cleaned up spec

* Wed May 25 2011 Götz Waschk <waschk@mandriva.org> 3.0.2-1
+ Revision: 679084
- new version

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 3.0.1-2
+ Revision: 677715
- rebuild to add gconftool as req

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 3.0.1-1
+ Revision: 659087
- update to new version 3.0.1

* Thu Apr 07 2011 Funda Wang <fwang@mandriva.org> 3.0.0.2-1
+ Revision: 651379
- update to new version 3.0.0.2

* Wed Apr 06 2011 Funda Wang <fwang@mandriva.org> 3.0.0.1-1
+ Revision: 650814
- try to find libmozjs
- update file list
- new version 3.0.0.1

* Fri Aug 06 2010 Funda Wang <fwang@mandriva.org> 2.29.1-8mdv2011.0
+ Revision: 566698
- drop BR on gir-repository

* Tue Jul 27 2010 Funda Wang <fwang@mandriva.org> 2.29.1-7mdv2011.0
+ Revision: 561839
- rebuild

* Mon Jun 28 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.1-6mdv2010.1
+ Revision: 549373
- rebuild with latest xulrunner

* Sun Apr 04 2010 Funda Wang <fwang@mandriva.org> 2.29.1-5mdv2010.1
+ Revision: 531046
- rebuild for new xulrunner

* Fri Apr 02 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.1-4mdv2010.1
+ Revision: 530777
- Remove old suggests, not needed anymore

* Wed Mar 31 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.1-3mdv2010.1
+ Revision: 530413
- requires gnome-session for session management (and integration in display manager)

* Wed Mar 24 2010 Götz Waschk <waschk@mandriva.org> 2.29.1-2mdv2010.1
+ Revision: 527081
- rebuild for new xulrunner

* Tue Mar 23 2010 Götz Waschk <waschk@mandriva.org> 2.29.1-1mdv2010.1
+ Revision: 526922
- new version
- drop patches 1,2

* Sat Mar 20 2010 Götz Waschk <waschk@mandriva.org> 2.29.0-3mdv2010.1
+ Revision: 525522
- fix build with new gjs (bug #58274)
- replace patch 1 by upstream version

  + Frederic Crozat <fcrozat@mandriva.com>
    - ensure there is no post by default

* Wed Mar 17 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.0-2mdv2010.1
+ Revision: 524312
- Source1: add support to select GNOME-Shell in display managers, as GNOME 3 Preview (idea from SUSE)

* Tue Feb 23 2010 Götz Waschk <waschk@mandriva.org> 2.29.0-1mdv2010.1
+ Revision: 510279
- new version
- fix build
- fix setting of the LD_LIBRARY_PATH for xulrunner

* Tue Feb 16 2010 Götz Waschk <waschk@mandriva.org> 2.28.0-4mdv2010.1
+ Revision: 506609
- disable Werror to make it build

* Wed Feb 03 2010 Thierry Vignaud <tv@mandriva.org> 2.28.0-3mdv2010.1
+ Revision: 499977
- requires glxinfo instead of mesa-demos

* Wed Jan 13 2010 Götz Waschk <waschk@mandriva.org> 2.28.0-2mdv2010.1
+ Revision: 490657
- rebuild for new libgnome-desktop

* Thu Oct 08 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 456027
- new version
- update deps

* Wed Sep 16 2009 Götz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 443455
- new version

* Sat Sep 05 2009 Götz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 432058
- new version

* Sat Aug 29 2009 Götz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 422175
- new version
- update deps
- add translations

* Mon Aug 17 2009 Götz Waschk <waschk@mandriva.org> 2.27.0-4mdv2010.0
+ Revision: 417151
- add missing dep on glxinfo

* Wed Aug 12 2009 Götz Waschk <waschk@mandriva.org> 2.27.0-3mdv2010.0
+ Revision: 415271
- remove devel deps again

* Wed Aug 12 2009 Michael Scherer <misc@mandriva.org> 2.27.0-2mdv2010.0
+ Revision: 415259
- add missing requires and suggest

* Tue Aug 11 2009 Götz Waschk <waschk@mandriva.org> 2.27.0-1mdv2010.0
+ Revision: 414732
- import gnome-shell


* Tue Aug 11 2009 Götz Waschk <waschk@mandriva.org> 2.27.0-1mdv2010.0
- initial package
