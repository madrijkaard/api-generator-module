package com.mxs.model;

import java.math.BigDecimal;
import java.time.LocalDateTime;

public class Example {

    private String codigo;
    private String descricao;
    private int status;
    private LocalDateTime dataCriacao;
    private LocalDateTime dataModificacao;
    private BigDecimal numeroGrande;

    public Example() {}

    public Example(String codigo, String descricao, int status, LocalDateTime dataCriacao, LocalDateTime dataModificacao, BigDecimal numeroGrande) {
        this.codigo = codigo;
        this.descricao = descricao;
        this.status = status;
        this.dataCriacao = dataCriacao;
        this.dataModificacao = dataModificacao;
        this.numeroGrande = numeroGrande;
    }

    public String getCodigo() {
        return codigo;
    }

    public void setCodigo(String codigo) {
        this.codigo = codigo;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public LocalDateTime getDataCriacao() {
        return dataCriacao;
    }

    public void setDataCriacao(LocalDateTime dataCriacao) {
        this.dataCriacao = dataCriacao;
    }

    public LocalDateTime getDataModificacao() {
        return dataModificacao;
    }

    public void setDataModificacao(LocalDateTime dataModificacao) {
        this.dataModificacao = dataModificacao;
    }

    public BigDecimal getNumeroGrande() {
        return numeroGrande;
    }

    public void setNumeroGrande(BigDecimal numeroGrande) {
        this.numeroGrande = numeroGrande;
    }
}
