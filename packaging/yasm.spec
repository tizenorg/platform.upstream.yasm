Name:           yasm
Version:        1.2.0
Release:        1
License:        BSD-2-Clause or BSD-3-Clause
Summary:        Yasm Modular Assembler
Url:            http://yasm.tortall.net/
Group:          System/Libraries
Source0:        %{name}-%{version}.tar.gz
Source1001: 	yasm.manifest
BuildRequires:  binutils-devel

%description
Yasm is a complete rewrite of the NASM assembler under the “new” BSD License (some portions are under other licenses, see COPYING for details).
Yasm currently supports the x86 and AMD64 instruction sets, accepts NASM and GAS assembler syntaxes, outputs binary, ELF32, ELF64, 32 and 64-bit Mach-O, RDOFF2, COFF, Win32, and Win64 object formats, and generates source debugging information in STABS, DWARF 2, and CodeView 8 formats.
Yasm can be easily integrated into Visual Studio 2005/2008 and 2010 for assembly of NASM or GAS syntax code into Win32 or Win64 object files.

%prep
%setup -q
cp %{SOURCE1001} .

%build
./configure --prefix=/usr

make %{?_smp_mflags}

%install
%make_install

%files
%manifest %{name}.manifest
%license COPYING
%{_bindir}/yasm
%{_bindir}/vsyasm
%{_bindir}/ytasm
%{_includedir}/libyasm-stdint.h
%{_includedir}/libyasm.h
%{_includedir}/libyasm/*
%{_mandir}/man1/yasm.1.gz
%{_mandir}/man7/yasm_arch.7.gz
%{_mandir}/man7/yasm_dbgfmts.7.gz
%{_mandir}/man7/yasm_objfmts.7.gz
%{_mandir}/man7/yasm_parsers.7.gz
