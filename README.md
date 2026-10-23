# Standby Pro · historical source baseline

This repository preserves the original **Standby Pro 1.0.0** Flutter app source from [Ghostzy0/standby-pro at 9ce5e167](https://github.com/Ghostzy0/standby-pro/tree/9ce5e1676a1eae2681037d75eb354cd76addf207). The existing community repository continues as the [improved Standby Pro](https://github.com/Ghostzy0/standby-pro).

This is an archival source baseline, not a production binary or a claim to recreate another app. `app/` is byte-for-byte the tracked upstream app at that commit; `PROVENANCE.json` records SHA256 for every included app file. Third-party reference images and the historical Git objects containing them are excluded because their redistribution rights are unknown. Original source copyright and MIT licence are retained.

## Verify and run

Use Flutter 3.41.9 / Dart 3.11.5. In `app/`:

```sh
flutter pub get --enforce-lockfile
flutter test
flutter analyze
```

On 23 October 2026 these checks passed in an isolated upstream checkout on Apple Silicon macOS: **10 tests**, analysis without issues. `BASELINE-CHECKS.txt` is the captured command output. This is source/widget evidence. No Android phone, signed iPhone, charging, lock-screen, battery or OLED acceptance is claimed.

Android needs JDK17 and Android SDK; iOS needs Xcode/CocoaPods and signing for a physical phone. This archive's Android release configuration uses a debug signing key: do not distribute it as a production release. No installable APK/IPA is supplied. Read [release notes and platform limits](RELEASE-NOTES.md).

## What the original provides

Single/Duo display layouts; Digital, Analog, Flip and Text clock faces; Aurora, Night Red, Solar and Matrix themes; stored display settings; night tint; small pixel shifts; Android foreground window keep-awake and brightness attempts.

Weather is fixed to London and the original high/low values are synthesized. Calendar and music metadata are sample data. There is no real calendar integration, iOS system bridge, WidgetKit/system StandBy integration or background alarm. The charger-labelled setting actually applies whenever the Android activity is open. See the improved repo for corrected data states, permission declarations and persistence handling.

## Privacy and licences

Preferences remain on device under `standby_settings_v1`. The original app automatically requests London weather from Open-Meteo, which sees device network/IP information. No analytics/accounts/ads. The original includes unused sensitive permission declarations; no native permission integration is implemented. The improved repo removes those declarations and makes weather opt-in.

MIT applies to the original app source. Flutter and Dart package dependencies have their own licences; use Flutter's generated licence inventory when building. Weather data is CC BY 4.0 and needs Open-Meteo attribution; the free API is limited to noncommercial use under [provider terms](https://open-meteo.com/en/terms). Do not monetise the free endpoint without appropriate service rights.

## Fidelity boundary

The upstream `assets/references` folder contained third-party Play listing captures. No licensed target binary, feature specification or observed third-party runtime was supplied. This repository establishes fidelity only to its pinned original Standby Pro source. A faithful third-party replica remains unestablished and is not advertised here.

AI setup prompt: “Clone Ghostzy0/standby-pro-baseline. Verify PROVENANCE.json, use Flutter 3.41.9, and run locked dependencies, tests and analysis. Report native SDK/signing gaps; do not call this a production phone build.”

## Support and maintenance

For active development, use the [existing Standby Pro issues](https://github.com/Ghostzy0/standby-pro/issues). This baseline intentionally retains historical behaviour. For security concerns, avoid posting sensitive information publicly; use GitHub's private reporting if enabled or contact the repository owner privately through an available channel.
