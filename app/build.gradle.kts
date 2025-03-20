import com.google.firebase.appdistribution.gradle.firebaseAppDistribution

val appDemoVersionCode: Int = project.property("APP_DEMO_VERSION_CODE").toString().toInt()
val releaseVersionCode: String = project.property("RELEASE_VERSION_NAME").toString()
val buildMavenSdkVersion: String = project.property("BUILD_MAVEN_SDK_VERSION").toString()
val appDistributionArchType = "APK"

plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.jetbrains.kotlin.android)
    alias(libs.plugins.firebase.appdistribution)
    alias(libs.plugins.google.services)
    alias(libs.plugins.compose.compiler)
}

apply(from = "firebase-app-distribution.gradle")
apply(from = "testing.gradle.kts")


android {
    namespace = "com.pditta.githubactions"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.pditta.githubactions"
        minSdk = 24
        targetSdk = 35
        versionCode = appDemoVersionCode
        versionName = releaseVersionCode

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"

    }

    buildTypes {
        getByName("debug") {
            isMinifyEnabled = false
            isDebuggable = true
        }
        getByName("release") {
            isMinifyEnabled = false
            isDebuggable = false
            //proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    kotlinOptions {
        jvmTarget = "17"
    }

    buildFeatures {
        viewBinding = true
        buildConfig = true
        compose = true
    }

    val firebaseReleaseNote = "GitHub Actions Example %s"

    flavorDimensions += listOf("example")

    productFlavors {
        create("dev") {
            dimension = "example"
            applicationIdSuffix = ".dev"

            firebaseAppDistribution {
                artifactType = appDistributionArchType
                releaseNotes = String.format(firebaseReleaseNote, "DEV")
                groups = "testers"
                serviceCredentialsFile = System.getenv("GITHUB_ACTIONS_EXAMPLE_APP_DISTR_FILE_KEY")
            }
        }
        create("uat") {
            dimension = "example"
            applicationIdSuffix = ".uat"

            firebaseAppDistribution {
                artifactType = appDistributionArchType
                releaseNotes = String.format(firebaseReleaseNote, "STAGE")
                groups = "testers"
                serviceCredentialsFile = System.getenv("GITHUB_ACTIONS_EXAMPLE_APP_DISTR_FILE_KEY")
            }
        }
        create("preProd") {
            dimension = "example"
            applicationIdSuffix = ".preprod"

            firebaseAppDistribution {
                artifactType = appDistributionArchType
                releaseNotes = String.format(firebaseReleaseNote, "PRE-PROD")
                groups = "testers"
                serviceCredentialsFile = System.getenv("GITHUB_ACTIONS_EXAMPLE_APP_DISTR_FILE_KEY")
            }
        }
        create("prod") {
            dimension = "example"
            applicationIdSuffix = ".prod"
            firebaseAppDistribution {
                artifactType = appDistributionArchType
                releaseNotes = String.format(firebaseReleaseNote, "PROD")
                groups = "testers"
                serviceCredentialsFile = System.getenv("GITHUB_ACTIONS_EXAMPLE_APP_DISTR_FILE_KEY")
            }
        }
    }
}

dependencies {

    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.lifecycle.runtime.ktx)
    implementation(libs.androidx.activity.compose)
    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.ui)
    implementation(libs.androidx.ui.graphics)
    implementation(libs.androidx.ui.tooling.preview)
    implementation(libs.androidx.material3)

    implementation(platform(libs.firebase.bom))

    implementation(project(":myTestLibrary"))

    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)
    androidTestImplementation(platform(libs.androidx.compose.bom))
    androidTestImplementation(libs.androidx.ui.test.junit4)

    debugImplementation(libs.androidx.ui.tooling)
    debugImplementation(libs.androidx.ui.test.manifest)
}