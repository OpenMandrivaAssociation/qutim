Name:		qutim
Version:	0.3.0
Release:	1
Summary:	qutIM - multiplatform multiprotocol (ICQ, Jabber etc) instant messenger
Group:		Networking/Instant messaging
License:	GPLv2
URL:		http://qutim.org/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	qt4-devel >= 4.4.0
BuildRequires:	idn-devel
BuildRequires:	gnutls-devel
BuildRequires:	cmake
BuildRequires:	SDL_sound-devel
BuildRequires:	SDLmm-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_gfx)
BuildRequires:	pkgconfig(SDL_mixer) pkgconfig(sdl)
BuildRequires:	jreen-devel >= 1.0.5
BuildRequires:	phonon-devel kdelibs4-devel qt4-linguist

%description
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger.


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
%define qutimdevelname %mklibname -d qutim

%package -n	%qutimdevelname
Summary:        qutim header files
Group:          Development/C
Provides:	%{name}-devel = %{version}-%{release}


%description -n %qutimdevelname
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger
header files.


%files -n %qutimdevelname
%{_includedir}/%{name}/adiumchat/*.h
%{_includedir}/%{name}/*.h
%{_includedir}/%{name}/simplecontactlist/*.h
%{_libdir}/libqutim.so
%{_libdir}/libqutim-adiumwebview.so
%{_datadir}/cmake/Modules/*


%prep
%setup -q
#%patch0 -p1


%build
export PATH="$PATH:/usr/lib/qt4/bin/"
%cmake_qt4	-DCMAKE_SKIP_RPATH=TRUE	\
		-DSYSTEM_JREEN=ON	\
		-DHAIKUNOTIFICATIONS=OFF \
		-DUNITYLAUNCHER=OFF	\
		-DUPDATER=OFF		\
		-DSDLSOUND=OFF		
#-DSDLMIXER_INCLUDE_DIR=%{_includedir}/SDL/
%make

%install
cd build/
%makeinstall_std

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}
%{_datadir}/apps/%{name}
%{_datadir}/apps/desktoptheme/default/icons/%{name}.svg
%{_libdir}/%{name}/plugins/*.so
%{_iconsdir}/*/*/*
