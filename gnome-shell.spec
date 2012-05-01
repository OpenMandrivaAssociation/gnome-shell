%define url_ver %(echo %{version}|cut -d. -f1,2)

# To make GNOME Shell extensions load, we need to get rid of DT_RUNPATH on /usr/bin/gnome-shell
# (see glibc bug #13945, GNOME bug #670477, Mageia bug #4523)
%define _disable_ld_enable_new_dtags 1

Summary:	Next generation GNOME desktop shell
Name:		gnome-shell
Version:	3.4.1
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
Url:		http://live.gnome.org/GnomeShell
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-shell/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: rootcerts
BuildRequires: polkit-1-devel
BuildRequires: pkgconfig(clutter-1.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(folks)
BuildRequires: pkgconfig(gcr-3)
BuildRequires: pkgconfig(gjs-1.0)
BuildRequires: pkgconfig(gl)
BuildRequires: pkgconfig(gnome-bluetooth-1.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libedataserverui-3.0)
BuildRequires: pkgconfig(libgnome-menu-3.0)
BuildRequires: pkgconfig(libmutter)
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnm-util)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(telepathy-glib)
BuildRequires: pkgconfig(telepathy-logger-0.2)
BuildConflicts: libevolution-data-server2-devel

Requires: at-spi2-atk
Requires: gjs
Requires: glxinfo
Requires: gnome-session
Requires: gtk+3.0
Requires: json-glib
Requires: librsvg
Requires: mutter

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
#autoreconf

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
%{_mandir}/man1/%{name}.1*

%files docs
%{_datadir}/gtk-doc/html/shell
%{_datadir}/gtk-doc/html/st

