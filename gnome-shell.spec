Summary: Next generation GNOME desktop shell
Name: gnome-shell
Version: 3.2.2.1
Release: 3
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/GnomeShell
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
#Patch0:	gnome-shell-3.1.4-bluetooth-libdir.patch

BuildRequires: intltool
BuildRequires: rootcerts
BuildRequires: polkit-1-devel
BuildRequires: pkgconfig(clutter-1.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(folks)
BuildRequires: pkgconfig(gjs-1.0)
#BuildRequires: pkgconfig(gnome-bluetooth-1.0)
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

Requires: at-spi2-atk
Requires: gjs
Requires: glxinfo
Requires: gnome-session
Requires: gtk+3.0
Requires: json-glib
Requires: librsvg
Requires: mutter

# missing typelib pkgs workaround
# remove once rpm auto prov/reqs
Requires: %{_lib}accountsservice-gir1.0
Requires: %{_lib}caribou-gir1.0
Requires: %{_lib}clutter-gtk-gir1.0
Requires: %{_lib}clutter-gir1.0
Requires: %{_lib}cogl-pango-gir1.0
Requires: %{_lib}cogl-gir1.0
Requires: %{_lib}folks-gir0.6
Requires: %{_lib}gdk_pixbuf-gir2.0
Requires: %{_lib}gee-gir1.0
Requires: %{_lib}gjs-gir1.0
Requires: %{_lib}gmenu-gir3.0
Requires: %{_lib}gnomekbd-gir3.0
Requires: %{_lib}jscore-gir3.0
Requires: %{_lib}json-glib-gir1.0
Requires: %{_lib}mutter-gir3.0
Requires: %{_lib}pangocairo-gir1.0
Requires: %{_lib}pangoft2-gir1.0
Requires: %{_lib}pango-gir1.0
Requires: %{_lib}soup-gir2.4
Requires: %{_lib}telepathy-logger-gir0.2

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

%prep
%setup -q
%apply_patches
#autoreconf

%build
#export LD_LIBRARY_PATH=%{_libdir}/gnome-bluetooth
%configure2_5x \
	--disable-static \
	--enable-compile-warnings=no \
	--disable-schemas-install

%make LIBS='-lgmodule-2.0'

%install
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'
%find_lang %{name}

%files -f %{name}.lang
%doc README 
%{_sysconfdir}/gconf/schemas/gnome-shell.schemas
%{_bindir}/*
%{_libdir}/%{name}
%{_libdir}/mozilla/plugins/*.so
%{_libexecdir}/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell-hotplug-sniffer
%{_libexecdir}/gnome-shell-perf-helper
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

