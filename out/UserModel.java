package com.mxs.model;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.UUID;

public class UserModel {

    private UUID code;
    private String username;
    private String password;
    private String email;
    private LocalDate dateOfBirth;
    private LocalDateTime registrationDate;
    private LocalDateTime lastModifiedDate;
    private boolean status;

    public UserModel() {}

    public UserModel(UUID code, String username, String password, String email, LocalDate dateOfBirth, LocalDateTime registrationDate, LocalDateTime lastModifiedDate, boolean status) {
        this.code = code;
        this.username = username;
        this.password = password;
        this.email = email;
        this.dateOfBirth = dateOfBirth;
        this.registrationDate = registrationDate;
        this.lastModifiedDate = lastModifiedDate;
        this.status = status;
    }

    public UUID getCode() {
    return code;
}

    public void setCode(UUID code) {
    this.code = code;
}

    public String getUsername() {
    return username;
}

    public void setUsername(String username) {
    this.username = username;
}

    public String getPassword() {
    return password;
}

    public void setPassword(String password) {
    this.password = password;
}

    public String getEmail() {
    return email;
}

    public void setEmail(String email) {
    this.email = email;
}

    public LocalDate getDateOfBirth() {
    return dateOfBirth;
}

    public void setDateOfBirth(LocalDate dateOfBirth) {
    this.dateOfBirth = dateOfBirth;
}

    public LocalDateTime getRegistrationDate() {
    return registrationDate;
}

    public void setRegistrationDate(LocalDateTime registrationDate) {
    this.registrationDate = registrationDate;
}

    public LocalDateTime getLastModifiedDate() {
    return lastModifiedDate;
}

    public void setLastModifiedDate(LocalDateTime lastModifiedDate) {
    this.lastModifiedDate = lastModifiedDate;
}

    public boolean getStatus() {
    return status;
}

    public void setStatus(boolean status) {
    this.status = status;
}
}
