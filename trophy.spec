Summary:	2D car racing action game
Summary(pl):	Dwuwymiarowa gra w wy¶cigi samochodowe
Name:		trophy
Version:	1.1.3
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/trophy/%{name}-%{version}-src.tar.gz
# Source0-md5:	45a8c6eec9ab5d110660a32416d1ec8f
URL:		http://trophy.sourceforge.net/
BuildRequires:	ClanLib-devel >= 0.6.0
BuildRequires:	ClanLib-devel < 0.7.0
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libGLcore.so.1

%description
TROPHY is a 2D car racing action game for Linux. There are many extras
which are... er... 'untypical' for racing games. So you can shoot at
other players for example.

%description -l pl
TROPHY to dwuwymiarowa gra w wy¶cigi samochodowe dla Linuksa. Ma wiele
dodatków, które s±... hm... nietypowe dla wy¶cigów. Mo¿na na przyk³ad
strzelaæ do innych graczy.

%prep
%setup -q -n %{name}-%{version}-src

%build
cd %{name}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%configure
%{__make} \
	CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions" \
	CPPFLAGS="`pkg-config --cflags clanCore-0.7`"

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
