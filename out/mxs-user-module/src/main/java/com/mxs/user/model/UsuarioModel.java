package com.mxs.user.model;

import jakarta.persistence.*;
import org.hibernate.annotations.GenericGenerator;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Entity(name = "usuario")
public class UsuarioModel {

    @Id
	@GeneratedValue(generator = "increment")
	@GenericGenerator(name = "increment", strategy = "increment")
	private Long id;
	@Column(name = "codigo")
	private String codigo;
    @Column(name = "nome_usuario")
	private String nomeUsuario;
    @Column(name = "senha")
	private String senha;
    @Column(name = "email")
	private String email;
    @Column(name = "aniversario")
	private LocalDate aniversario;
    @Column(name = "data_tempo_cadastro")
	private LocalDateTime dataTempoCadastro;
    @Column(name = "data_tempo_ultima_modificacao")
	private LocalDateTime dataTempoUltimaModificacao;
    @Column(name = "status")
	private boolean status;

    public UsuarioModel() {}

    public UsuarioModel(String codigo, String nomeUsuario, String senha, String email, LocalDate aniversario, LocalDateTime dataTempoCadastro, LocalDateTime dataTempoUltimaModificacao, boolean status) {
        this.codigo = codigo;
        this.nomeUsuario = nomeUsuario;
        this.senha = senha;
        this.email = email;
        this.aniversario = aniversario;
        this.dataTempoCadastro = dataTempoCadastro;
        this.dataTempoUltimaModificacao = dataTempoUltimaModificacao;
        this.status = status;
    }

    public String getCodigo() {
	    return codigo;
	}

    public void setCodigo(String codigo) {
	    this.codigo = codigo;
	}

    public String getNomeUsuario() {
	    return nomeUsuario;
	}

    public void setNomeUsuario(String nomeUsuario) {
	    this.nomeUsuario = nomeUsuario;
	}

    public String getSenha() {
	    return senha;
	}

    public void setSenha(String senha) {
	    this.senha = senha;
	}

    public String getEmail() {
	    return email;
	}

    public void setEmail(String email) {
	    this.email = email;
	}

    public LocalDate getAniversario() {
	    return aniversario;
	}

    public void setAniversario(LocalDate aniversario) {
	    this.aniversario = aniversario;
	}

    public LocalDateTime getDataTempoCadastro() {
	    return dataTempoCadastro;
	}

    public void setDataTempoCadastro(LocalDateTime dataTempoCadastro) {
	    this.dataTempoCadastro = dataTempoCadastro;
	}

    public LocalDateTime getDataTempoUltimaModificacao() {
	    return dataTempoUltimaModificacao;
	}

    public void setDataTempoUltimaModificacao(LocalDateTime dataTempoUltimaModificacao) {
	    this.dataTempoUltimaModificacao = dataTempoUltimaModificacao;
	}

    public boolean getStatus() {
	    return status;
	}

    public void setStatus(boolean status) {
	    this.status = status;
	}
}
