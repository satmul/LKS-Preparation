# Android

## Disassemble

JADX

## SMALI

A SMALI file contains source code written in the assembly language used by Smali assembler/disassembler for Android platform. This file is usually generated from disassembled Dalvik (DEX) or Java (CLASS) bytecode of an Android application using smali/baksmali disassembler.

Basically this is the assembly of java.

We could patch Smali to gain unauthorized access / action if the APK is not properly secured with integrity check.

Integrity check? to secure the APK by rechecking the signature of the recompiled APK and compare it with the actual signature, if the signature is different then the APK won't run.

## Strings.xml

APK stores sensitive data / endpoints on strings.xml file. 

http://pallergabor.uw.hu/androidblog/dalvik_opcodes.html