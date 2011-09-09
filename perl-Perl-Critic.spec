Name:           perl-Perl-Critic
Version:        1.105
Release:        2%{?dist}
Summary:        Critique Perl source code for best-practices

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Perl-Critic/
Source0:        http://search.cpan.org/CPAN/authors/id/E/EL/ELLIOTJS/Perl-Critic-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(Module::Build)
BuildRequires:  perl(B::Keywords) >= 1.05
BuildRequires:  perl(Config::Tiny) >= 2
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Pluggable) >= 3.1
BuildRequires:  perl(PPI) >= 1.205
BuildRequires:  perl(String::Format) >= 1.13
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Test::Memory::Cycle)
BuildRequires:  perl(Readonly) >= 1.03
BuildRequires:  perl(Exception::Class) >= 1.23
# BuildRequires:  perl(Email::Address)
# BuildRequires:  perl(Regexp::Parser)
BuildRequires:  perl(Test::Deep)
# Author tests
BuildRequires:  perl(Test::Perl::Critic)
# BuildRequires:  perl(Test::Kwalitee)
# BuildRequires:  aspell-en
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Test::Spelling)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

Requires:       perl(Module::Pluggable) >= 3.1
Requires(hint): perl(Perl::Tidy)

### auto-added brs!
BuildRequires:  perl(strict)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(charnames)
BuildRequires:  perl(File::Spec::Unix)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(lib)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(overload)
BuildRequires:  perl(base)
BuildRequires:  perl(version)
BuildRequires:  perl(Carp)
BuildRequires:  perl(warnings)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Pod::PlainText)
BuildRequires:  perl(Pod::Select)
BuildRequires:  perl(English)

# don't "provide" private Perl libs
%global _use_internal_dependency_generator 0
%global __deploop() while read FILE; do /usr/lib/rpm/rpmdeps -%{1} ${FILE}; done | /bin/sort -u
%global __find_provides /bin/sh -c "%{__grep} -v '%_docdir' | %{__grep} -v '%{perl_vendorarch}/.*\\.so$' | %{__deploop P}"
%global __find_requires /bin/sh -c "%{__grep} -v '%_docdir' | %{__deploop R}"

%description
Perl::Critic is an extensible framework for creating and applying coding
standards to Perl source code. Essentially, it is a static source code
analysis engine. Perl::Critic is distributed with a number of
Perl::Critic::Policy modules that attempt to enforce various coding
guidelines. Most Policy modules are based on Damian Conway's book Perl
Best Practices. However, Perl::Critic is not limited to PBP and will
even support Policies that contradict Conway. You can enable, disable,
and customize those Polices through the Perl::Critic interface. You can
also create new Policy modules that suit your own tastes.


%prep
%setup -q -n Perl-Critic-%{version}

find . -type f -exec chmod -c -x {} +

%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*


%check
# Additional requirements of author tests:
#   Test::Perl::Critic, Test::Kwalitee
TEST_AUTHOR=0 ./Build test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes LICENSE README TODO.pod examples/ extras/ tools/
%{_bindir}/*
%{perl_vendorlib}/Perl/
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3pm*


%changelog
* Mon May  3 2010 Marcela Mašláňová <mmaslano@redhat.com> - 1.105-2
- remove optional BR, and switch off author tests. aspell is here only for
 author test.
- rhbz#586154
- Related: rhbz#543948

* Wed Oct  7 2009 Stepan Kasal <skasal@redhat.com> - 1.105-1
- new upstream version
- update build requires

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.098-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun May 17 2009 Chris Weyl <cweyl@alumni.drew.edu> 1.098-1
- "neaten" filtering
- auto-update to 1.098 (by cpan-spec-update 0.01)
- added a new br on perl(strict) (version 0)
- added a new br on perl(Scalar::Util) (version 0)
- added a new br on perl(File::Temp) (version 0)
- added a new br on perl(Pod::Usage) (version 0)
- added a new br on perl(File::Find) (version 0)
- added a new br on perl(PPI::Token::Whitespace) (version 1.203)
- added a new br on perl(charnames) (version 0)
- added a new br on perl(PPI::Document::File) (version 1.203)
- added a new br on perl(File::Spec::Unix) (version 0)
- added a new br on perl(List::Util) (version 0)
- added a new br on perl(lib) (version 0)
- added a new br on perl(Getopt::Long) (version 0)
- added a new br on perl(Exporter) (version 0)
- added a new br on perl(Test::More) (version 0)
- added a new br on perl(overload) (version 0)
- added a new br on perl(base) (version 0)
- added a new br on perl(version) (version 0)
- added a new br on perl(Carp) (version 0)
- added a new br on perl(warnings) (version 0)
- added a new br on perl(PPI::Document) (version 1.203)
- added a new br on perl(File::Basename) (version 0)
- added a new br on perl(PPI::Token::Quote::Single) (version 1.203)
- added a new br on perl(File::Spec) (version 0)
- added a new br on perl(File::Path) (version 0)
- added a new br on perl(Pod::PlainText) (version 0)
- added a new br on perl(Pod::Select) (version 0)
- added a new br on perl(PPI::Node) (version 1.203)
- added a new br on perl(English) (version 0)

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.092-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.092-1
- update to 1.092

* Sun Mar 09 2008 Chris Weyl <cweyl@alumni.drew.edu> 1.082-1
- update to 1.082
- resolve BZ#431577
- add t/ examples/ extras/ tools/, and filter

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.080-3
- Rebuild for perl 5.10 (again)

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.080-2
- add missing BR: perl-Exception-Class

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.080-1
- bump to 1.080

* Mon Jan 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.053-2
- rebuild for new perl

* Sat Jun 16 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.053-1
- Update to 1.053.

* Tue Mar 20 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.05-1
- Update to 1.05.

* Thu Feb 15 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.03-1
- Update to 1.03.

* Fri Jan 26 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-2
- Bumping release (forgot to commit sources and .cvsignore changes).

* Fri Jan 26 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.01-1
- Update to 1.01.
- New build requirement: perl(Test::Memory::Cycle).

* Thu Jan 25 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.23-2
- perl(Set::Scalar) is no longer required.

* Wed Jan 24 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.23-1
- Update to 0.23.
- New requirement: perl(B::Keywords).
- Author tests coverage improved.

* Sun Dec 17 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.22-2
- Enabled author tests.
- BR perl(HomeDir).

* Sun Dec 17 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.22-1
- Update to 0.22.

* Sat Nov 11 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.21-1
- Update to 0.21.
- New BR: perl(Set::Scalar).

* Sat Sep 16 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0.2-1
- First build.
