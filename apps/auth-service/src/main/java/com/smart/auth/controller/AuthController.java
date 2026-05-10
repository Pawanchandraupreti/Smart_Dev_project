package com.smart.auth.controller;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;
import java.util.Random;

@RestController
public class AuthController {
    private static final Logger logger = LoggerFactory.getLogger(AuthController.class);
    private final Random random = new Random();

    @GetMapping("/health")
    public Map<String, String> health() {
        return Map.of("status", "UP");
    }

    @GetMapping("/login")
    public Map<String, String> login() {
        if (random.nextDouble() > 0.3) {
            logger.info("Login successful for user_{}", random.nextInt(100));
            return Map.of("status", "success");
        } else {
            logger.warn("Login failed - invalid credentials");
            return Map.of("status", "failed");
        }
    }

    @GetMapping("/simulate-error")
    public Map<String, String> simulateError() {
        logger.error("Database connection lost in Auth Service!");
        return Map.of("status", "error");
    }
}
