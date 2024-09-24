{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.11") {} }:
  let python-packages = ps: with ps; [
    black
    ipywidgets
    jupyterlab
    matplotlib
    mypy
    nltk
    seaborn
    scipy
    numpy
    openpyxl
    pandas
  ];
  in
  pkgs.mkShell {
    nativeBuildInputs = with pkgs; [
    	(python3.withPackages python-packages)
    ];
  }

