%define name gnome-shell
%define version 2.27.0
%define release %mkrel 3

Summary: Next generation GNOME desktop shell
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
License: GPLv2+ and LGPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/GnomeShell
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mutter-devel
BuildRequires: gjs-devel
BuildRequires: libgstreamer-plugins-base-devel >= 0.10.16
BuildRequires: clutter-gtk-devel
BuildRequires: librsvg-devel
BuildRequires: gnome-menus-devel
BuildRequires: dbus-glib-devel
BuildRequires: libgnomeui2-devel
BuildRequires: gir-repository
Requires: mutter
Requires: gjs
Requires: gir-repository
# for testing without --replace 
Suggests:  x11-server-xephyr xterm
Suggests:  xlogo xeyes 
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

%build
%configure2_5x
#gw parallel build broken in 2.27.0
make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post
%define schemas gnome-shell
%if %mdkversion < 200900
%post_install_gconf_schemas %schemas
%endif

%preun
%preun_uninstall_gconf_schemas %schemas


%files
%defattr(-,root,root)
#%doc README NEWS AUTHORS ChangeLog
%_sysconfdir/gconf/schemas/gnome-shell.schemas
%_bindir/%name
%_libdir/%name
%_libdir/mutter/plugins/libgnome-shell.la
%_libdir/mutter/plugins/libgnome-shell.so
%_datadir/applications/%name.desktop
%_datadir/%name

