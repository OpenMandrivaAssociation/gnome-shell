%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)
# To make GNOME Shell extensions load, we need to get rid of DT_RUNPATH on /usr/bin/gnome-shell
# (see glibc bug #13945, GNOME bug #670477, Mageia bug #4523)
%define _disable_ld_enable_new_dtags 1
%define debug_package %{nil}

Summary:	Next generation GNOME desktop shell
Name:		gnome-shell
Version:	3.30.1
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
Url:		http://live.gnome.org/GnomeShell
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-shell/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool >= 0.40
BuildRequires:	rootcerts
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(caribou-1.0)
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gcr-3)
BuildRequires:	pkgconfig(gjs-1.0) >= 1.35.4
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gnome-bluetooth-1.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	pkgconfig(libecal-1.2)
BuildRequires:	pkgconfig(libgnome-menu-3.0) >= 3.6.0
BuildRequires:  pkgconfig(libmutter-3)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libnm-glib)
BuildRequires:	pkgconfig(libnm-gtk)
BuildRequires:	pkgconfig(libnm-util)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(telepathy-logger-0.2)

BuildRequires:  meson
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libcroco-0.6)
#BuildRequires:  pkgconfig(mutter-clutter-2)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:	pkgconfig(libnm)
BuildRequires:  sassc
BuildRequires:  pkgconfig(mutter-clutter-3)

Requires:	at-spi2-atk
Requires:	gjs
Requires:	glxinfo
Requires:	gnome-session
Requires:	gtk+3.0
Requires:	json-glib
Requires:	librsvg
Requires:	mutter

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
Summary:	Documentation for %{name}
Group:		Books/Computer books
BuildArch:	noarch

%description docs
This package contains the documentation for %{name}.

%prep
%setup -q
%apply_patches

%build
%meson -Denable-documentation=true
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc README.md NEWS HACKING.md
%{_bindir}/*
%{_sysconfdir}/xdg/autostart/gnome-shell-overrides-migration.desktop
%{_libdir}/%{name}
%{_libdir}/mozilla/plugins/*.so
%{_libexecdir}/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell-hotplug-sniffer
%{_libexecdir}/gnome-shell-perf-helper
%{_libexecdir}/gnome-shell-portal-helper
%{_libexecdir}/gnome-shell-overrides-migration.sh
%{_datadir}/applications/org.gnome.Shell.desktop
%{_datadir}/applications/evolution-calendar.desktop
%{_datadir}/applications/gnome-shell-extension-prefs.desktop
#{_datadir}/applications/gnome-shell-wayland.desktop
%{_datadir}/applications/org.gnome.Shell.PortalHelper.desktop
%{_datadir}/dbus-1/services/org.gnome.Shell.PortalHelper.service
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Extensions.xml
%{_datadir}/GConf/gsettings/gnome-shell-overrides.convert
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.gschema.override
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
%{_datadir}/gnome-control-center/keybindings/*%{name}*.xml
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/xdg-desktop-portal/portals/%{name}.portal
%{_userunitdir}/gnome-shell-wayland.target
%{_userunitdir}/gnome-shell-x11.target
%{_userunitdir}/gnome-shell.service

#files docs
#{_datadir}/gtk-doc/html/shell
#{_datadir}/gtk-doc/html/st

