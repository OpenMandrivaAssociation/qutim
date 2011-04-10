%define _disable_ld_as_needed 1

%define name qutim
%define release %mkrel 1

%define coreversion		0.2.0.529
%define icqversion		0.2.0.136
%define ircversion		0.2.0.38
%define jabberversion		0.2.0.431
%define mrimversion		0.2.0.146
%define vkontakteversion	0.2.0.40
%define yandexnarodversion	0.2.0.21
%define histmanversion		0.2.0.13
%define plugmanversion		0.2.0.151
%define imagepubversion		10
%define kdeversion		31
%define msnversion		6
%define urlpreviewversion	12
%define cchkversion		0.0.7
%define twitterversion		4

Name:           %{name}
Version:        %{coreversion}
Release:        %{release}
Summary:        qutIM - multiplatform multiprotocol (ICQ, Jabber etc) instant messenger
Group:          Networking/Instant messaging
License:        GPLv2
URL:            http://qutim.org/
Source0:        %{name}-%{coreversion}.tar.bz2
Source1:	qutim-emoticons-0.2.0.tar.bz2
Source2:	qutim-langs-0.2.0.tar.bz2
Source3:	qutim-sounds-0.2.0.tar.bz2
Source4:	qutIM.desktop
Source5:	TributeToQIP.tar.bz2
Source6:	qutim-glass.tar.bz2
Source7:	connectioncheck-%cchkversion.tar.bz2
Source8:	additional_plugins.tar.bz2
Patch0:		%{name}-0.2.0-x86_64.patch
Patch1:		qutim-msn-3-cmake.patch
BuildRoot:      %{_tmppath}/%{name}-%{coreversion}-%{release}-buildroot
BuildRequires:  qt4-devel >= 4.4.0
BuildRequires:  idn-devel
BuildRequires:  gnutls-devel
BuildRequires:  cmake
BuildRequires:  phonon-devel kdelibs4-devel

%description
qutIM - multiplatform multiprotocol (ICQ, Jabber) instant messenger.

%package -n %{name}-icq
Summary:  	ICQ plugin for qutIM
Group:          Networking/Instant messaging
Version:  	%{icqversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-icq
ICQ plugin for qutIM.

%package -n %{name}-jabber
Summary: 	Jabber plugin for qutIM
Group:          Networking/Instant messaging
Version: 	%{jabberversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-jabber
Jabber plugin for qutIM.

%package -n %{name}-irc
Summary:  	IRC plugin for qutIM
Group:          Networking/Instant messaging
Version:  	%{ircversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-irc
IRC plugin for qutIM.

%package -n %{name}-mrim
Summary:  	Mail.ru plugin for qutIM
Group:          Networking/Instant messaging
Version:  	%{mrimversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-mrim
Mail.ru plugin for qutIM.

%package -n %{name}-msn
Summary: 	MSN plugin for qutIM
Group:          Networking/Instant messaging
Version: 	%{msnversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-msn
MSN plugin for qutIM.

%package -n %{name}-vkontakte
Summary: 	Vkontakte.ru plugin for qutIM
Group:          Networking/Instant messaging
Version: 	%{vkontakteversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-vkontakte
Vkontakte.ru plugin for qutIM.

%package -n %{name}-imagepub
Summary: 	Image publishing services plugin for qutIM
Group:          Networking/Instant messaging
Version: 	%{imagepubversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-imagepub
Image publishing services plugin for qutIM.

%package -n %{name}-urlpreview
Summary: 	Prewiew URLs in messages plugin for qutIM
Group:      	Networking/Instant messaging
Version: 	%{urlpreviewversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-urlpreview
Prewiew URLs in messages plugin for qutIM.

%package -n %{name}-yandexnarod
Summary: 	Yandex.narod.ru plugin for qutIM
Group:      	Networking/Instant messaging
Version: 	%{yandexnarodversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-yandexnarod
Yandex.narod.ru plugin for qutIM. Requires narod.ru account.

%package -n %{name}-connectioncheck
Summary: 	Connection check plugin for qutIM
Group:		Networking/Instant messaging
Version: 	%{cchkversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-connectioncheck
Connection check plugin for qutIM.

%package -n %{name}-twitter
Summary: 	Twitter plugin for qutIM
Group:      	Networking/Instant messaging
Version: 	%{twitterversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-twitter
Twitter plugin for qutIM.

%package -n %{name}-histman
Summary: 	History manager plugin for qutIM
Group:      	Networking/Instant messaging
Version: 	%{histmanversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-histman
History manager plugin for qutIM. Import history from clients
like QIP, Miranda, Pidgin, Kopete, Gajim, Psi and others.

%package -n %{name}-plugman
Summary: 	Plugin manager for qutIM
Group:      	Networking/Instant messaging
Version: 	%{plugmanversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-plugman
Plugin manager for qutIM. Allow install additional themes,
icon packs and other useful staff.

%package -n %{name}-kde-integration
Summary: 	KDE integration plugin set for qutIM
Group:          Networking/Instant messaging
Version: 	%{kdeversion}
Requires: 	%{name} = %{coreversion}

%description -n %{name}-kde-integration
KDE integration plugin set for qutIM.

%package -n task-%{name}
Summary: 	Task for qutIM with Jabber & ICQ plugins
Group:          Networking/Instant messaging
Version: 	%{coreversion}
Requires: 	%{name} = %{coreversion}
Requires: 	%{name}-icq = %{icqversion}
Requires: 	%{name}-jabber = %{jabberversion}

%description -n task-%{name}
Metapackage for qutIM + Jabber & ICQ plugins.

%prep
%setup -q
%patch0 -p0
pushd plugins
tar xvjf %SOURCE8
tar xvjf %SOURCE7
popd
%patch1 -p0

tar xvjf %SOURCE1
tar xvjf %SOURCE2
tar xvjf %SOURCE3

%build
%cmake_qt4 -DCMAKE_SKIP_RPATH=TRUE
%make

pushd ../plugins/icq
%qmake_qt4
%make
popd

pushd ../plugins/jabber
%cmake_qt4 -DGNUTLS=1
%make
popd

pushd ../plugins/irc
%qmake_qt4
%make
popd

pushd ../plugins/kde-integration
%cmake_kde4
%make
popd

pushd ../plugins/mrim
%cmake_qt4
%make
popd

pushd ../plugins/msn
%cmake_qt4
%make
popd

pushd ../plugins/vkontakte
%qmake_qt4
%make
popd

pushd ../plugins/imagepub
%qmake_qt4
%make
popd

pushd ../plugins/urlpreview
%qmake_qt4
%make
popd

pushd ../plugins/yandexnarod
%qmake_qt4
%make
popd

pushd ../plugins/connectioncheck
%qmake_qt4
%make
popd

pushd ../plugins/histman
%qmake_qt4
%make
popd

pushd ../plugins/twitter
%qmake_qt4
%make
popd

pushd ../plugins/plugman
%cmake_qt4
%make
popd

%install
rm -rf %buildroot
%__install -D -m 0644 "icons/qutim_64.png" "%{buildroot}%{_datadir}/pixmaps/%{name}.png"
%__install -d "%{buildroot}%{_bindir}"
%__install -d "%{buildroot}%{_desktopdir}"
%__install -d "%{buildroot}%{_libdir}/%{name}"
%__install -d "%{buildroot}%{_datadir}/%{name}/languages/ru"
%__install -d "%{buildroot}%{_datadir}/%{name}/webkitstyle"

cp "build/%{name}" "%{buildroot}%{_bindir}/%{name}"
cp %SOURCE4 "%{buildroot}%{_desktopdir}/%{name}.desktop"
cp "plugins/icq/libicq.so" "%{buildroot}%{_libdir}/%{name}/libicq.so"
cp "plugins/jabber/build/libjabber.so" "%{buildroot}%{_libdir}/%{name}/libjabber.so"
cp "plugins/irc/libirc.so" "%{buildroot}%{_libdir}/%{name}/libirc.so"
cp "plugins/mrim/build/libmrim.so" "%{buildroot}%{_libdir}/%{name}/libmrim.so"
cp "plugins/msn/build/libmsn.so" "%{buildroot}%{_libdir}/%{name}/libmsn.so"
cp "plugins/vkontakte/libvkontakte.so" "%{buildroot}%{_libdir}/%{name}/libvkontakte.so"
cp "plugins/imagepub/libimagepub.so" "%{buildroot}%{_libdir}/%{name}/libimagepub.so"
cp "plugins/urlpreview/liburlpreview.so" "%{buildroot}%{_libdir}/%{name}/liburlpreview.so"
cp "plugins/yandexnarod/libyandexnarod.so" "%{buildroot}%{_libdir}/%{name}/libyandexnarod.so"
cp "plugins/connectioncheck/libconnectioncheck.so" "%{buildroot}%{_libdir}/%{name}/libconnectioncheck.so"
cp "plugins/histman/libhistman.so" "%{buildroot}%{_libdir}/%{name}/libhistman.so"
cp "plugins/twitter/libtwitter.so" "%{buildroot}%{_libdir}/%{name}/libtwitter.so"
cp "plugins/plugman/build/libplugman.so" "%{buildroot}%{_libdir}/%{name}/libplugman.so"

cp plugins/kde-integration/build/lib/libkde*.so %{buildroot}%{_libdir}/%{name}/

cp -R "emoticons" "%{buildroot}%{_datadir}/%{name}/"
cp -R languages/ru/*.qm "%{buildroot}%{_datadir}/%{name}/languages/ru"
cp -R "sounds" "%{buildroot}%{_datadir}/%{name}/"
cd "%{buildroot}%{_datadir}/%{name}/webkitstyle"
tar xvjf %SOURCE5
tar xvjf %SOURCE6

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}

%files -n %{name}-icq
%defattr(-,root,root)
%{_libdir}/%{name}/libicq.so

%files -n %{name}-irc
%defattr(-,root,root)
%{_libdir}/%{name}/libirc.so

%files -n %{name}-mrim
%defattr(-,root,root)
%{_libdir}/%{name}/libmrim.so

%files -n %{name}-jabber
%defattr(-,root,root)
%{_libdir}/%{name}/libjabber.so

%files -n %{name}-msn
%defattr(-,root,root)
%{_libdir}/%{name}/libmsn.so

%files -n %{name}-vkontakte
%defattr(-,root,root)
%{_libdir}/%{name}/libvkontakte.so

%files -n %{name}-imagepub
%defattr(-,root,root)
%{_libdir}/%{name}/libimagepub.so

%files -n %{name}-urlpreview
%defattr(-,root,root)
%{_libdir}/%{name}/liburlpreview.so

%files -n %{name}-yandexnarod
%defattr(-,root,root)
%{_libdir}/%{name}/libyandexnarod.so

%files -n %{name}-connectioncheck
%defattr(-,root,root)
%{_libdir}/%{name}/libconnectioncheck.so

%files -n %{name}-twitter
%defattr(-,root,root)
%{_libdir}/%{name}/libtwitter.so

%files -n %{name}-histman
%defattr(-,root,root)
%{_libdir}/%{name}/libhistman.so

%files -n %{name}-plugman
%defattr(-,root,root)
%{_libdir}/%{name}/libplugman.so

%files -n %{name}-kde-integration
%defattr(-,root,root)
%{_libdir}/%{name}/libkde*.so

%files -n task-%{name}
%defattr(-,root,root)
