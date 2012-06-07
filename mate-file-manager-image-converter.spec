Summary:	Caja extension to mass resize images
Name:		mate-file-manager-image-converter
Version:	1.2.0
Release:	1
Group:		Graphical desktop/GNOME
License:	GPLv2+
URL:		http://pub.mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libcaja-extension)

Requires:	ImageMagick
Provides:	caja-image-converter = %{version}=%{release}

%description
Adds a "Resize Images..." menu item to the context menu of all images. This
opens a dialog where you set the desired image size and file name. A click
on "Resize" finally resizes the image(s) using ImageMagick's convert tool.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang caja-image-converter

%files -f caja-image-converter.lang
%doc AUTHORS COPYING
%{_datadir}/caja-image-converter
%{_libdir}/caja/extensions-2.0/*.so

