# Android

## Disassemble

JADX


## Development Languages

- Java
- Kotlin
- Flutter (Dart code (libapp.so), cant directly be disassembled because it relies on Dart VM )
- React Native (Could be disassembled if the index.android.bundle is not heavily obfuscated / packed)
- Objective C
- Xamarin (.dll)
- Cordova (html css js)
- manymore....

## ADB (Android Debug Bridge)

ADB is a tool that let you communicate with android device such as installing / debugging apps.

commonly used feature:

    - adb shell (gain access into device shell)
    - adb logcat (preview logs that comes from APK)


## SMALI

A SMALI file contains source code written in the assembly language used by Smali assembler/disassembler for Android platform. This file is usually generated from disassembled Dalvik (DEX) or Java (CLASS) bytecode of an Android application using smali/baksmali disassembler.

Basically this is the assembly of java.

We could patch Smali to gain unauthorized access / action if the APK is not properly secured with integrity check.

Integrity check? to secure the APK by rechecking the signature of the recompiled APK and compare it with the actual signature, if the signature is different then the APK won't run.


## Strings.xml

some developer stores sensitive data / endpoints on strings.xml file. 

http://pallergabor.uw.hu/androidblog/dalvik_opcodes.html



## Frida / Dynamic Instrumentation

Dynamic Instrumentation is a technique that used to patch APK on runtime to bypass any detection such as root detection / SSL pinning or modifying return value of any function.

How to install frida? https://medium.com/my-infosec-write-ups/frida-installation-40f52845ae98

Frida example:

```
//change role from regular user to admin

Java.perform(function() {
    let MainActivity = Java.use("com.blackbear.lksnapk.MainActivity");
    MainActivity["checkStatus"].implementation = function (role, x) {
        console.log('checkStatus is called' + ', ' + 'role: ' + role + ', ' + 'x: ' + x);
        let ret = this.checkStatus("admin", x);
        console.log('Role: ' + ret);
        return ret;
    };
});
```

Frida collection scripts: https://codeshare.frida.re/