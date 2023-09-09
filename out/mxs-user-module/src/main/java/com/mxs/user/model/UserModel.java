package com.mxs.user.model;

import javax.persistence.*;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.UUID;

@Entity(name = "user")
public class UserModel {

    @Column(name = "code", nullable = true)
	private UUID code;
    @Column(name = "username", nullable = true)
	private String username;
    @Column(name = "password", nullable = true)
	private String password;
    @Column(name = "email", nullable = true)
	private String email;
    @Column(name = "date_of_birth", nullable = true)
	private LocalDate dateOfBirth;
    @Column(name = "registration_date", nullable = true)
	private LocalDateTime registrationDate;
    @Column(name = "last_modified_date", nullable = true)
	private LocalDateTime lastModifiedDate;
    @Column(name = "status", nullable = true)
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
