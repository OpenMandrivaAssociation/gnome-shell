%define name gnome-shell
%define version 3.0.2
%define release %mkrel 1

Summary: Next generation GNOME desktop shell
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: gnome-shell-session
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/GnomeShell
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mutter-devel >= 3.0.0
BuildRequires: gjs-devel >= 0.7.11
BuildRequires: libgstreamer-plugins-base-devel >= 0.10.16
BuildRequires: clutter-devel >= 1.5.15
BuildRequires: gnome-menus-devel
BuildRequires: dbus-glib-devel
BuildRequires: gnome-desktop3-devel >= 2.90.0
BuildRequires: libtelepathy-glib-devel >= 0.13.12
BuildRequires: libtelepathy-logger-devel >= 0.2.4
BuildRequires: gtk+3.0-devel >= 3.0.0
BuildRequires: evolution-data-server-devel >= 1.2.0
BuildRequires: gsettings-desktop-schemas-devel >= 0.1.7
BuildRequires: intltool
BuildRequires: polkit-1-devel
BuildRequires: libcanberra-devel
BuildRequires: pulseaudio-devel
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
export LD_LIBRARY_PATH=%xulrunner_mozappdir
%configure2_5x --enable-compile-warnings=no \
 --disable-static --disable-schemas-install
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %name

mkdir -p %{buildroot}/%{_datadir}/gnome-shell/xdg-override/autostart
cp -f %{buildroot}/%{_datadir}/applications/gnome-shell.desktop %{buildroot}/%{_datadir}/gnome-shell/xdg-override/autostart

install -m 755 %{SOURCE1} %{buildroot}/%{_datadir}/gnome-shell/

# wmsession session file
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmsession.d
cat << EOF > $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmsession.d/11GNOME3
NAME=GNOME 3 Preview
ICON=gnome-logo-icon-transparent.png
DESC=GNOME Environment
EXEC=%{_datadir}/gnome-shell/gnome-shell-session
SCRIPT:
exec %{_datadir}/gnome-shell/gnome-shell-session
EOF


%clean
rm -rf %{buildroot}

%define schemas gnome-shell

%if %mdkversion < 200900
%post
%post_install_gconf_schemas %schemas
%endif

%preun
%preun_uninstall_gconf_schemas %schemas

%files -f %name.lang
%defattr(-,root,root)
%doc README 
%_sysconfdir/gconf/schemas/gnome-shell.schemas
%_sysconfdir/X11/wmsession.d/*
%_bindir/*
%_libdir/%name
%{_libexecdir}/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell-perf-helper
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%_datadir/applications/%name.desktop
%_datadir/%name
%_mandir/man1/%name.1*
