%define _disable_ld_no_undefined 1

%define snapshot 0
%if %{snapshot}
%define gitdate 20121026
%define gitrev	d41951	
%endif

Name:		qutim
%if %{snapshot}
Version:        0.3.1
Release:        0.%{gitdate}.1
%else
Version:	0.3.1
Release:	1
%endif
Summary:	qutIM - multiplatform multiprotocol (ICQ, Jabber etc) instant messenger
Group:		Networking/Instant messaging
License:	GPLv2
URL:		http://qutim.org/
%if %{snapshot}
Source0:	%{name}-%{version}-%{gitdate}.tar.gz
%else
Source0:	%{name}-%{version}.tar.bz2
%endif
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	qt4-devel
BuildRequires:	qt4-linguist
BuildRequires:	SDLmm-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	pkgconfig(libidn)
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_gfx)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	jreen-devel >= 1.0.5
BuildRequires:	pkgconfig(phonon)

Patch0:		telepathy-qt4-telepathyqt-upstream.patch

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

#------------------------------------------------------------------
%define major 0
%define libname %mklibname qutim %{major}

%package -n	%{libname}
Summary:	Tunneling of IPv6 over UDP through NATs
Group:		Networking/Instant messaging

%description -n %{libname}
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger.

%files -n %{libname}
%{_libdir}/libqutim.so.%{major}*


#------------------------------------------------------------------
%define qadium %mklibname qutim-adiumwebview %{major}

%package -n	%{qadium}
Summary:	Tunneling of IPv6 over UDP through NATs
Group:		Networking/Instant messaging

%description -n %{qadium}
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger.

%files -n %{qadium}
%{_libdir}/libqutim-adiumwebview.so.%{major}*


#------------------------------------------------------------------
%define qutimdevelname %mklibname -d %{name}

%package -n	%{qutimdevelname}
Summary:	qutIM header files
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{qutimdevelname}
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger
header files.

%files -n %{qutimdevelname}
%{_includedir}/%{name}/adiumchat/*.h
%{_includedir}/%{name}/*.h
%{_includedir}/%{name}/simplecontactlist/*.h
%{_libdir}/libqutim.so
%{_libdir}/libqutim-adiumwebview.so
%{_datadir}/cmake/Modules/*

%prep
%setup -q
%patch0 -p1

#rm -rf ./protocols/jabber/jreen ./plugins/plugman/3rdparty ./protocols/oscar/3rdparty 
#./core/3rdparty/qxt

%build
#-DUNITYLAUNCHER=OFF	\
export PATH="$PATH:/usr/lib/qt4/bin/"
%cmake_kde4	-DCMAKE_SKIP_RPATH=TRUE	\
		-DHAIKUNOTIFICATIONS=OFF \
		-DASTRAL=off		\
		-DPLUGMAN=off		\
		-DCMAKE_SKIP_RPATH:BOOL=ON \
		-DUPDATER=OFF		\
		-DSYSTEM_JREEN=ON	\
		-DSDLSOUND=OFF
%make

%install
%makeinstall_std -C build
