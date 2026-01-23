package com.example.controller;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/metodos")
public class MetodosController {

    // Responde a GET e OPTIONS (automaticamente pelo Spring/navegador)
    @GetMapping
    public ResponseEntity<String> handleGet() {
        return ResponseEntity.ok("GET method handled successfully!");
    }

    // Responde a POST
    @PostMapping
    public ResponseEntity<String> handlePost() {
        return ResponseEntity.ok("POST method handled successfully!");
    }

    // Responde a PUT
    @PutMapping
    public ResponseEntity<String> handlePut() {
        return ResponseEntity.ok("PUT method handled successfully!");
    }

    // Responde a DELETE
    @DeleteMapping
    public ResponseEntity<String> handleDelete() {
        return ResponseEntity.ok("DELETE method handled successfully!");
    }

    // Responde a TRACE (requer configuração de segurança para ser ativado)
    // O Spring Boot padrão desabilita TRACE por segurança.
    // Para teste local, você pode forçar a resposta manualmente, mas não é trivial.

    // Responde a CONNECT
    // CONNECT é um método de proxy e não é implementado facilmente em um RestController padrão.

}