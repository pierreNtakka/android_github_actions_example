import org.gradle.configurationcache.extensions.capitalized

plugins {
    alias(libs.plugins.android.library)
    alias(libs.plugins.jetbrains.kotlin.android)
    alias(libs.plugins.compose.compiler)
}

apply(from = "maven-distribution.gradle")

android {
    namespace = "com.pditta.mytestlibrary"
    compileSdk = 35

    defaultConfig {
        minSdk = 21

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
        consumerProguardFiles("consumer-rules.pro")
    }


    buildTypes {
        getByName("debug") {
            isMinifyEnabled = false
        }
        getByName("release") {
            isMinifyEnabled = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }


    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    buildFeatures {
        viewBinding = true
        buildConfig = true
        compose = true
    }

    kotlinOptions {
        jvmTarget = "17"
    }

    flavorDimensions += listOf("example")

    productFlavors {
        create("dev") {
            dimension = "example"
        }
        create("uat") {
            dimension = "example"
        }
        create("preProd") {
            dimension = "example"
        }
        create("prod") {
            dimension = "example"
        }
    }


    libraryVariants.all {
        this.outputs
            .filter { this.buildType.name == "release" }
            .map { it as com.android.build.gradle.internal.api.LibraryVariantOutputImpl }
            .forEach { output ->
                this.productFlavors.get(0)
                val buildType = this.buildType.name
                var aarfileName =
                    "myTestLibrary-${this.productFlavors[0].name}${buildType.capitalized()}"
                aarfileName += ".aar"
                println("aarFilenName=$aarfileName}")
                output.outputFileName = aarfileName
            }
    }

}

dependencies {

    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.appcompat)
    implementation(libs.material)
    implementation(libs.androidx.activity.compose)
    implementation(platform(libs.androidx.compose.bom))

    testImplementation(libs.junit)
    androidTestImplementation(libs.androidx.junit)
    androidTestImplementation(libs.androidx.espresso.core)
}