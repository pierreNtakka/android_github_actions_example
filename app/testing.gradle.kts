tasks.register("cleanTask") {
    group = "verification"
    description = "Clean project"

    doLast {
        exec {
            workingDir = file("../")
            commandLine("./gradlew", "clean")
        }
    }
}

tasks.register("testTask") {
    group = "verification"
    description = "Test project"

    doLast {
        exec {
            workingDir = file("../")
            commandLine("./gradlew", "test")
        }
    }
}

tasks.register("testing") {
    group = "verification"
    description = "Run clean and test"

    dependsOn("cleanTask", "testTask")
}