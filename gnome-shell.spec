%define name gnome-shell
%define version 2.29.1
%define release %mkrel 5

Summary: Next generation GNOME desktop shell
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Source1: gnome-shell-session
# different fix for https://bugzilla.gnome.org/show_bug.cgi?id=573413
Patch0: gnome-shell-2.29.0-fix-xulrunner-libdir.patch
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/GnomeShell
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mutter-devel >= 2.28.0
BuildRequires: gjs-devel >= 0.6
BuildRequires: libgstreamer-plugins-base-devel >= 0.10.16
BuildRequires: clutter-gtk-devel
BuildRequires: librsvg-devel
BuildRequires: gnome-menus-devel
BuildRequires: dbus-glib-devel
BuildRequires: gnome-desktop-devel
BuildRequires: gir-repository
BuildRequires: intltool
Requires: mutter
Requires: gjs
Requires: gir-repository
Requires: glxinfo
Requires: gnome-session
BuildRequires: xulrunner-devel
%{?xulrunner_libname:Requires: %xulrunner_libname}

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
sed -i "s^xXULRUNNERDIRx^%xulrunner_mozappdir^" src/gnome-shell.in

%build
#gw else it does not find libmozjs.so
export LD_LIBRARY_PATH=%xulrunner_mozappdir
%configure2_5x --enable-compile-warnings=no \
 --disable-static 
%make

%install
rm -rf %{buildroot}
GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std
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
%_bindir/%name
%_libdir/%name
%_libdir/mutter/plugins/libgnome-shell.la
%_libdir/mutter/plugins/libgnome-shell.so
%_datadir/applications/%name.desktop
%_datadir/%name
%_mandir/man1/%name.1*
