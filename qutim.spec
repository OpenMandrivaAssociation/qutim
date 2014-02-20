%define _disable_ld_no_undefined 1

Summary:	qutIM - multiplatform multiprotocol (ICQ, Jabber etc) instant messenger
Name:		qutim
Version:	0.3.2
Release:	1
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		http://qutim.org/
Source0:	http://qutim.org/dwnl/68/%{name}-%{version}.tar.xz
Patch0:		telepathy-qt4-telepathyqt-upstream.patch
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	qt4-assistant
BuildRequires:	qt4-linguist
BuildRequires:	aspell-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	qt4-devel
BuildRequires:	SDLmm-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(libjreen)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_gfx)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(SDL_ttf)
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(vreen)

%description
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger.

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/apps/desktoptheme/default/icons/%{name}.svg
%{_libdir}/%{name}/plugins/*.so
%{_iconsdir}/*/*/*

#----------------------------------------------------------------------------

%define major 0
%define libname %mklibname qutim %{major}

%package -n	%{libname}
Summary:	qutIM shared library
Group:		Networking/Instant messaging

%description -n %{libname}
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger.

%files -n %{libname}
%{_libdir}/libqutim.so.%{major}*

#----------------------------------------------------------------------------

%define chat_major 1
%define libadiumchat %mklibname qutim-adiumchat %{chat_major}

%package -n	%{libadiumchat}
Summary:	qutIM shared library
Group:		Networking/Instant messaging

%description -n %{libadiumchat}
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger.

%files -n %{libadiumchat}
%{_libdir}/libqutim-adiumchat.so.%{chat_major}*

#----------------------------------------------------------------------------

%define libadiumwebview %mklibname qutim-adiumwebview %{major}

%package -n	%{libadiumwebview}
Summary:	qutIM shared library
Group:		Networking/Instant messaging

%description -n %{libadiumwebview}
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger.

%files -n %{libadiumwebview}
%{_libdir}/libqutim-adiumwebview.so.%{major}*

#----------------------------------------------------------------------------

%define libsimplecontactlist %mklibname qutim-simplecontactlist %{major}

%package -n	%{libsimplecontactlist}
Summary:	qutIM shared library
Group:		Networking/Instant messaging

%description -n %{libsimplecontactlist}
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger.

%files -n %{libsimplecontactlist}
%{_libdir}/libqutim-simplecontactlist.so.%{major}*

#----------------------------------------------------------------------------

%define qutimdevelname %mklibname -d %{name}

%package -n	%{qutimdevelname}
Summary:	qutIM header files
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{libadiumchat} = %{EVRD}
Requires:	%{libadiumwebview} = %{EVRD}
Requires:	%{libsimplecontactlist} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{qutimdevelname}
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger
header files.

%files -n %{qutimdevelname}
%{_includedir}/%{name}/*.h
%{_includedir}/%{name}/adiumchat/*.h
%{_includedir}/%{name}/adiumwebview/*.h
%{_includedir}/%{name}/simplecontactlist/*.h
%{_libdir}/libqutim.so
%{_libdir}/libqutim-adiumchat.so
%{_libdir}/libqutim-adiumwebview.so
%{_libdir}/libqutim-simplecontactlist.so
%{_datadir}/cmake/Modules/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4 \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DSYSTEM_JREEN=ON \
	-DSYSTEM_VREEN=ON \
	-DASTRAL=OFF \
	-DDOCKTILE=OFF \
	-DHAIKUNOTIFICATIONS=OFF \
	-DMACINTEGRATION=OFF \
	-DMAEMO5INTEGRATION=OFF \
	-DMOBILEABOUT=OFF \
	-DMOBILECONTACTINFO=OFF \
	-DMOBILENOTIFICATIONSSETTINGS=OFF \
	-DMOBILESETTINGSDIALOG=OFF \
	-DMOBILITY=OFF \
	-DOFFTHERECORD=OFF \
	-DPLUGMAN=OFF \
	-DSDLSOUND=OFF \
	-DSYMBIANINTEGRATION=OFF \
	-DUPDATER=OFF \
	-DWININTEGRATION=OFF
%make

%install
%makeinstall_std -C build
