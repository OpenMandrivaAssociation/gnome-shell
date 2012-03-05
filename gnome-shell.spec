Summary: Next generation GNOME desktop shell
Name: gnome-shell
Version: 3.2.2.1
Release: 1
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/GnomeShell
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
Source1: gnome-shell-session

BuildRequires: intltool
BuildRequires: polkit-1-devel
BuildRequires: pkgconfig(clutter-1.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(folks)
BuildRequires: pkgconfig(gjs-1.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libcanberra)
#BuildRequires: pkgconfig(libedataserver-1.2)
BuildRequires: pkgconfig(libedataserverui-3.0)
BuildRequires: pkgconfig(libgnome-menu-3.0)
BuildRequires: pkgconfig(libmutter)
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnm-util)
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(telepathy-glib)
BuildRequires: pkgconfig(telepathy-logger-0.2)

Requires: mutter
Requires: gjs
Requires: gir-repository
Requires: glxinfo
Requires: gnome-session

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

%build
#export LD_LIBRARY_PATH=%xulrunner_mozappdir
%configure2_5x \
	--disable-static \
	--enable-compile-warnings=no \
	--disable-schemas-install

%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

mkdir -p %{buildroot}/%{_datadir}/gnome-shell/xdg-override/autostart
cp -f %{buildroot}/%{_datadir}/applications/gnome-shell.desktop %{buildroot}/%{_datadir}/gnome-shell/xdg-override/autostart

install -m 755 %{SOURCE1} %{buildroot}/%{_datadir}/gnome-shell/

# wmsession session file
mkdir -p %{buildroot}%{_sysconfdir}/X11/wmsession.d
cat << EOF > %{buildroot}%{_sysconfdir}/X11/wmsession.d/11GNOME3
NAME=GNOME3 Desktop
ICON=gnome-logo-icon-transparent.png
DESC=GNOME Environment
EXEC=%{_datadir}/gnome-shell/gnome-shell-session
SCRIPT:
exec %{_datadir}/gnome-shell/gnome-shell-session
EOF

%define schemas gnome-shell

%files -f %{name}.lang
%doc README 
%{_sysconfdir}/gconf/schemas/gnome-shell.schemas
%{_sysconfdir}/X11/wmsession.d/*
%{_bindir}/*
%{_libdir}/%{name}
%{_libexecdir}/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell-perf-helper
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

