# -*- sh -*-
__example()
{
    local cur prev opts
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"
    opts="--hello --world --help" # which autocomplition do i want
    if [[ ${prev} == "--hello" ]]; then
        COMPREPLY=( $(compgen -W "world morning kuku" -- ${cur}) ) # when i type --hello and press tab it will complit me m corld morning kuku
        return 0
    fi
    if [[ ${prev} == "--world" ]]; then
        COMPREPLY=( $(compgen -W "is_heating" -- ${cur}) )
        return 0
    fi
    if [[ ${prev} == "--help" ]]; then
        COMPREPLY=( $(compgen -W "me" -- ${cur}) )
        return 0
    fi
    if [[ ${cur} == * ]] ; then
        COMPREPLY=( $(compgen -W "${opts}" -- ${cur}) )
        return 0
    fi
}
complete -F __example  #<program name>
