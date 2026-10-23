# Packaging patch log

## v1.0.0-baseline.2

Independent remote recovery of the new baseline repository found three original Gradle wrapper files omitted by Git's generated ignore rules during the curated import. The provenance manifest correctly rejected that incomplete checkout. This patch force-includes the original `app/android/gradle/wrapper/gradle-wrapper.jar`, `app/android/gradlew`, and `app/android/gradlew.bat` bytes. It changes no Dart/Kotlin/Swift source, UI or settings. All83 app files now match upstream9ce5e1676a1eae2681037d75eb354cd76addf207.

The source archive under baseline.1 in this separate repository is superseded; the exact original baseline release in the existing standby-pro repository is unaffected. No published history or tag was rewritten.
